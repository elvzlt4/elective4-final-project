import requests
from bs4 import BeautifulSoup
import csv

url = 'https://shopee.ph/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
for item in soup.find_all('div', class_='item'):
    title = item.find('h2').text
    price = item.find('span', class_='price').text
    data.append([title, price])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])
    writer.writerows(data)
