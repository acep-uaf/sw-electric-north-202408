import pandas as pd

# save AETR generation data to file
(pd.read_csv('https://raw.githubusercontent.com/acep-uaf/aetr-web-book-2024/main/data/final_data/generation.csv')
    .dropna(subset=['generation'])
    .query('generation >= 0')
    .to_csv('data/raw/aetr_generation.csv', index=False))
