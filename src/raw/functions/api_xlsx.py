import requests

def xlsx_url_to_file(xlsx_url, file):
    try:
        response = requests.get(xlsx_url)
        if response.status_code == 200:
            with open(file, 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    xlsx_url_to_file()
