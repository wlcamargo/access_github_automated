import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GH_TOKEN')
owner = os.getenv('OWNER')
repo = os.getenv('GITHUB_REPOSITORY')

if not token or not owner or not repo:
    print("Make sure the environment variables GH_TOKEN, OWNER, and REPO are correctly set in the .env file.")
    exit()

excel_file = "/mnt/c/Users/walla/OneDrive/collabs.xlsx"  # Replace with your actual link

try:
    df = pd.read_excel(excel_file, engine='openpyxl')  # Specify the engine
    print(df)
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit()

expected_columns = {'username', 'permission'}
if not expected_columns.issubset(df.columns):
    print(f"The Excel spreadsheet must contain the columns: {expected_columns}")
    exit()

for index, row in df.iterrows():
    username = row['username']
    permission = 'pull'

    if pd.isna(username) or pd.isna(permission):
        print(f"Row {index + 1} is missing data. Skipping this row.")
        continue

    url = f'https://api.github.com/repos/{owner}/{repo}/collaborators/{username}'

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }

    data = {
        'permission': permission  # Can be 'pull', 'push', 'admin'
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Invitation sent successfully to {username}!")
    elif response.status_code == 204:
        print(f"Invitation was already sent or {username} is already a collaborator.")
    else:
        print(f"Failed to send invitation to {username}: {response.status_code}")
        print(response.json())
