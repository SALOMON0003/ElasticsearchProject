import json
from elasticsearch import helpers
from elasticsearch_client import client

index_name = 'search-djnm'

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            doc = json.loads(line)
            yield {
                '_index': index_name,
                '_source': {
                    'link' : doc.get('link', ''),
                    'headline': doc.get('headline', ''),
                    'category' : doc.get('category', ''),
                    'short_description' : doc.get('short_description', ''),
                    'authors' : doc.get('authors', ''),
                    'date' : doc.get('date', '')
                }
            }

if __name__ == '__main__':
    file_path = 'dataset/News_Category_Dataset_v3.json'
    try:
        response = helpers.bulk(client, load_data(file_path))
        print('Insertion effectuer avec success')
        print(f"{response[0]} documents indexés.")
    except Exception as e:
        print('Erreur lors de l\'insertion : ', e)
