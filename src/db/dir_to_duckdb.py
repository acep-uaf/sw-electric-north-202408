import ibis
from glob import iglob
import os

# point towards files to vaccuum into the database
# data_dir = 'data/derived'
# db_dir = 'data/db/test.ddb'

def data_to_db(data_dir, database_filepath):
    db_uri = 'duckdb://' + database_filepath

    # open a connection (or create) the database
    con = ibis.connect(db_uri)
    con.load_extension('spatial')

    # find all csv and geojson files in the directory
    csv_files = iglob(os.path.join(data_dir, '*.csv'))
    geojson_files = iglob(os.path.join(data_dir, '*.geojson'))

    # loop to write csvs into the database
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        table_name = os.path.splitext(file_name)[0]
        con.create_table(
            table_name,
            con.read_csv(table_name=table_name, source_list=file_path),
            overwrite=True)

    # loop to write geojsons into the database
    for file_path in geojson_files:
        file_name = os.path.basename(file_path)
        table_name = os.path.splitext(file_name)[0]
        con.create_table(
            table_name,
            con.read_geo(table_name=table_name, source=file_path),
            overwrite=True)

    con.disconnect()


if __name__ == "__main__": 
    data_to_db(data_dir='data/raw', database_filepath='data/db/raw.ddb')


