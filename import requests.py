import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Step 1: Send a request to the webpage with headers
url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10021161/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table by its class and ID
table = soup.find('div', {'class': 'table-wrap anchored whole_rhythm', 'id': 'pgph.0000154.t003'})

# Extract table data into a list
table_data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th', 'td']):
        row_data.append(cell.text.strip().encode('utf-8').decode('utf-8'))
    table_data.append(row_data)

# Convert the list of lists into a DataFrame
df = pd.DataFrame(table_data)

# Remove empty rows and columns
df = df.replace('', pd.NA).dropna(how='all', axis=1).dropna(how='all')

# Set the first row as column headers
df.columns = df.iloc[0]
df = df[1:]

# Save the DataFrame to a CSV file
df.to_csv('table_data.csv', index=False)

print("CSV file has been created successfully.")