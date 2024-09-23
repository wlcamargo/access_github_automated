import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv('GH_TOKEN')
owner = os.getenv('OWNER')
repo = os.getenv('GITHUB_REPOSITORY')
planilha = os.getenv('LINK_PLANILHA')

if not token or not owner or not repo:
    print("Make sure the environment variables GH_TOKEN, OWNER, and REPO are correctly set in the .env file.")
    exit()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)

spreadsheet_url = planilha
sheet = client.open_by_url(spreadsheet_url).sheet1

try:
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    print(df)
except Exception as e:
    print(f"Error reading the Google Sheets data: {e}")
    exit()

expected_columns = {'username'}
if not expected_columns.issubset(df.columns):
    print(f"The Google Sheets spreadsheet must contain the columns: {expected_columns}")
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
        'permission': permission 
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Invitation sent successfully to {username}!")
    elif response.status_code == 204:
        print(f"Invitation was already sent or {username} is already a collaborator.")
    else:
        print(f"Failed to send invitation to {username}: {response.status_code}")
        print(response.json())
