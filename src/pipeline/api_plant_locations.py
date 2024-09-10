import requests

url = "https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/master/workbooks/Energy_Stats_Infrastructure_2021.xlsx"
response = requests.get(url)

# Save the response content to a file
with open('data/raw/Energy_Stats_Infrastructure_2021.xlsx', 'wb') as f:
    f.write(response.content)

