import geopandas as gpd

full_url = 'https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0/query?outFields=*&where=1%3D1&f=geojson'
server = 'https://maps.commerce.alaska.gov/server/rest/services'
service = 'Community_Related/Community_Locations_and_Boundaries/MapServer'
layer = '0'
query = 'query?outFields=*&where=1%3D1&f=geojson'

url = f"{server}/{service}/{layer}/{query}"

community_locations = gpd.read_file(url)
    
