import ibis
from glob import iglob
import os
import pandas as pd

# point towards files to vaccuum into the database
# data_dir = 'data/derived'
# db_dir = 'data/db/test.ddb'

con = ibis.postgres.connect(host='localhost', port=5432, database='testing', user='ian', password=None)


# def data_to_db(data_dir):

#     # find all csv files in the directory
#     csv_files = iglob(os.path.join(data_dir, '*.csv'))

#     # loop to write csvs into the database
#     for file_path in csv_files:
#         file_name = os.path.basename(file_path)
#         table_name = os.path.splitext(file_name)[0]
#         con.create_table(
#             table_name,
#             con.read_csv(table_name=table_name, path=file_path),
#             overwrite=True)


#     con.disconnect()


# if __name__ == "__main__": 
#     data_to_db(data_dir='data/raw/')

aetr = ibis.read_csv('data/raw/aetr_generation.csv')

con.create_table(
    name='ibis_read_csv_u6eatviovnfktirieiu6wivbhu',
    obj=aetr,
    overwrite=True)

