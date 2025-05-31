from fastapi import FastAPI, Query
from elasticsearch import Elasticsearch
from elasticsearch_client import client
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
@app.get('/search')
def search(q: str = Query(..., min_length=1)):
    query_body = {
        'query': {
            'multi_match': {
                'query' : q,
                'fields' : ['headline', 'short_description', 'authors']
            }
        }
    }

    response = client.search(index = 'search-djnm', body = query_body)
    hits = response['hits']['hits']
    results = [
        {
            'link': h['_source']['link'],
            'headline' : h['_source']['headline'],
            'category': h['_source']['category'],
            'short_description' : h['_source']['short_description'],
            'authors' : h['_source']['authors'],
            'date': h['_source']['date'],
        } for h in hits]
    return {'results': results}

@app.get('/search_with_filters')
def search_with_filters(
        q: str = Query(...),
        category: Optional[List[str]] = Query(None),
        author: str = Query(None)
):
    filters = []
    if category:
        filters.append({'terms': {'category.keyword': category}})
    if author:
        filters.append({'term': {'authors.keyword': author}})
    query_body = {
        'query': {
            'bool': {
                'must': {
                    'multi_match': {
                        'query': q,
                        'fields': ['headline', 'short_description']
                    }
                },
                'filter': filters
            }
        }
    }
    response = client.search(index = 'search-djnm', body = query_body)
    hits = response["hits"]["hits"]
    results = [
        {
            "link": h["_source"]["link"],
            "headline": h["_source"]["headline"],
            "short_description": h["_source"]["short_description"],
            "authors": h["_source"]["authors"],
            "category": h["_source"]["category"],
            "date": h["_source"]["date"],
            "score": h["_score"]
        }for h in hits]

    return {"results": results}


@app.get("/search_highlight")
def search_highlight(q: str = Query(...)):
    query_body = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["headline", "short_description"]
            }
        },
        "highlight": {
            "pre_tags": ["<mark>"],
            "post_tags": ["</mark>"],
            "fields": {
                "headline": {},
                "short_description": {}
            }
        }
    }

    response = client.search(index="search-djnm", body=query_body)
    hits = response["hits"]["hits"]
    results = []

    for h in hits:
        source = h["_source"]
        highlight = h.get("highlight", {})
        results.append({
            "headline": highlight.get("headline", [source["headline"]])[0],
            "short_description": highlight.get("short_description", [source["short_description"]])[0],
            "authors": source["authors"],
            "category": source["category"],
            "date": source["date"],
            "score": h["_score"]
        })

    return {"results": results}

@app.get("/search_sorted")
def search_sorted(q: str = Query(...), sort_by_date: bool = False):
    body = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["headline", "short_description"]
            }
        }
    }

    if sort_by_date:
        body["sort"] = [
            {
                "date":
                    {
                        "order": "desc"
                    }
            }
        ]

    response = client.search(index="search-djnm", body=body)
    hits = response["hits"]["hits"]
    results = [
        {
            "headline": h["_source"]["headline"],
            "short_description": h["_source"]["short_description"],
            "date": h["_source"]["date"],
            "score": h["_score"]
        }for h in hits]

    return {"results": results}
