import pandas as pd

lookup_interties = pd.read_csv('data/raw/es_lookup_interties.csv')

interties = lookup_interties[lookup_interties['Current ID'] == True].drop(columns=['Communities Intertied'])

interties.to_csv('data/derived/interties.csv')
