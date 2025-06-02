import requests

def download_csv(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"CSV file downloaded successfully and saved as {save_path}")
    else:
        print(f"Failed to download CSV. Status code: {response.status_code}")
