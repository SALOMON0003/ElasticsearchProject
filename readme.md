# Projet Moteur de Recherche Personnalisé sur un Grand Volume de Documents (avec Elasticsearch)

- Creation de compte dans https://cloud.elastic.co
- Creation d'un deployment de elasticsearch et de kibana
- Recuperation des api-key, endpoint, username et password
- Test des api avec python
- Collecte de dataset dans kaggle https://kaggle.com/datasets
- Telechargement du dataset news headlines HuffPost
- L'architecture du projet:  

ProjetMoteurDeRecherche/  
│  
├── elasticsearch_client.py  
├── ingest_data.py   
├── search.py  
├── readme.md  
├── info.txt  
├── dataset/  
│   └── News_Category_Dataset_v3.json  
├── frontend/  
│   └── public/  
│   └── src/  

- Insertion des 209 527 documents dans mon index
- Creation de notre api de rechercher avec FastApi 
- Creation du Front avec React js