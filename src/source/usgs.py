import zipfile
import os
from urllib.request import urlretrieve




def zip_to_file(zip_url, zip_path, path_to_save):
    urlretrieve(zip_url, zip_path) # download from url, save to filepath as zip

    os.makedirs(path_to_save, exist_ok=True) # target for extracted directory

    with zipfile.ZipFile(zip_path, 'r') as zip_ref: # extract and save to directory
        zip_ref.extractall(path_to_save)



zip_to_file(
    zip_url = 'https://eerscmap.usgs.gov/uswtdb/assets/data/uswtdbGeoJSON.zip',
    zip_path = 'data/source/uswtdb.zip',
    path_to_save = 'data/source/uswtdb'
    )

# It looks like this is all Census data repackaged?
# Not sure the value of this dataset, but preserving nonetheless
zip_to_file(
    zip_url = 'https://prd-tnm.s3.amazonaws.com/StagedProducts/GovtUnit/Shape/GOVTUNIT_Alaska_State_Shape.zip',
    zip_path = 'data/source/usgs_nbd.zip',
    path_to_save = 'data/source/usgs_nbd'
)
