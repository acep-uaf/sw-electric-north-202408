import pandas as pd

lookup_interties = pd.read_csv('data/derived/lookup_interties.csv')

current_interties = lookup_interties[lookup_interties['Current ID'] == True].drop(columns=['Communities Intertied'])

current_interties.to_csv('data/derived/current_interties.csv')
