from elasticsearch import Elasticsearch

CLOUD_ID = 'https://31ead02aebad462e9792c5d759d2c6e6.us-central1.gcp.cloud.es.io:443'
API_KEY = 'dEV1NERaY0JJRWtkSVdzUkNMVWI6R2RyQ25sRjlVWTAxU1d0V3lGa0taUQ=='

client = Elasticsearch(
    CLOUD_ID,
    api_key= API_KEY
)
