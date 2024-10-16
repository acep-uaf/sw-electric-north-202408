import zipfile
import os
from urllib.request import urlretrieve


zip_url = 'https://fema-femadata.s3.amazonaws.com/Partners/ORNL/USA_Structures/Alaska/Deliverable20230728AK.zip'
zip_path = 'data/source/fema_usa_structures.zip'

urlretrieve(zip_url, zip_path)

path_to_save = 'data/source/fema_usa_structures'
os.makedirs(path_to_save, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(path_to_save)


