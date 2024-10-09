import ibis
import geopandas as gpd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# set up connection
con = ibis.postgres.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)


load = gpd.read_file('data/raw/cares_transmission.geojson')
