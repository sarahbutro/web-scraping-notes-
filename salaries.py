import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2014&agency=931'

response = requests.get(url)
html = response.content 
soup = BeautifulSoup(html)

results_table = soup.find('table', attrs = {'id': 'grdEmployees'})

output = []

for row in results_table.findAll('tr'):
    output_row = []
    
    for cell in row.findAll('td'):
        output_row.append(cell.text)

    output.append(output_row)    

handle = open('salaries.csv', 'w')
outfile = csv.writer(handle)

outfile.writerows(output)