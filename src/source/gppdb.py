import requests
import zipfile
import os
from urllib.request import urlretrieve

# response = requests.request(
#     "GET",
#     "https://wri.prod.ckan.datopian.com/api/3/action/package_show?id=c767c803-5294-4cd4-b6fa-d79db94f8cc5",
    
# )
# data = response.json()
# print(data)

# from data:
# 'https://wri.prod.ckan.datopian.com/dataset/c767c803-5294-4cd4-b6fa-d79db94f8cc5/resource/eeb5705e-9fd4-4662-bae9-2f38af8fce1f/download/globalpowerplantdatabasev130.zip'



zip_url = 'https://wri.prod.ckan.datopian.com/dataset/c767c803-5294-4cd4-b6fa-d79db94f8cc5/resource/4340a48b-f5a3-4925-b194-0455873eeb62/download/globalpowerplantdatabasev110.zip'
zip_path = 'data/source/gppdb.zip'

urlretrieve(zip_url, zip_path)

path_to_save = 'data/source/gppdb'
os.makedirs(path_to_save, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(path_to_save)

print('WARNING!!! This is the old version of the Global Power Plant Database. Use for testing purposes only!')
