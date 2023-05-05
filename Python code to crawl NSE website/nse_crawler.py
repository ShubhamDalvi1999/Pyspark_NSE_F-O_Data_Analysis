import requests
from bs4 import BeautifulSoup
import datetime

# URL to the webpage with the download link
url = 'https://www.nseindia.com/all-reports-derivatives'

# Create a session to store cookies for subsequent requests
session = requests.Session()
response = session.get(url)

# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the F&O-BhavCopy file CSV for the previous 2 days
today = datetime.date.today()

for i in range(1, 3):
    date = (today - datetime.timedelta(days=i)).strftime('%d-%b-%Y').upper()
    file_name = f"fo{date}bhav.csv.zip"
    link = soup.find('a', {'href': file_name})
    if link:
        break

if not link:
    print('No download link found')
    exit()

# Construct the download URL and download the file
download_url = f"https://www.nseindia.com{link['href']}"
response = session.get(download_url)

# Save the file to a local directory
local_path = '/path/to/local/directory/'
local_filename = file_name[:-4]  # Remove .zip extension
with open(local_path + local_filename, 'wb') as f:
    f.write(response.content)

print(f'Downloaded {local_filename} to {local_path}')