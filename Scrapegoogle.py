from bs4 import BeautifulSoup
import requests
import csv

search_query = input("What would you like to search? ")
filename = input("What would you like to name the exported csv file? ")
source = requests.get(f"https://www.google.com/search?safe=off&source=hp&ei=SaqfXL2CGoGUtQXGiqwo&q={search_query}&btnK=Google+Search&oq={search_query}&gs_l=psy-ab.3...1396.2099..2179...0.0..0.100.643.5j2......0....1..gws-wiz.....0..35i39j0j0i131j0i10.U7HM6InUXJA").text

soup = BeautifulSoup(source, 'lxml')


#EXPORT RESULTS TO CSV FILE
csv_file = open(f'{filename}.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'url', 'date', 'summary'])

 
#print(soup.prettify)
#results = soup.find_all('div', class_='g', limit=3)
for results in soup.find_all('div', class_='g', limit=10):

    headline = results.a.text

    weblink = results.find('cite').text

    summary = results.find('span', class_="st").text

    csv_writer.writerow([headline, weblink, summary])


