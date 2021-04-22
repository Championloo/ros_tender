import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pprint import pprint
from bs4 import BeautifulSoup
import xlwt
import csv
import re
import urllib
from pprint import pprint

resp = requests.get('https://zakupki.gov.ru/epz/ktru/start/startPage.html', verify=False)
soup = BeautifulSoup(resp.text, 'lxml')
# print(soup)
section = soup.find('section', class_='content content-search-registry-block')
# print(section)
divs = section.find_all('div', class_='col-3 mb-3 rubricator-list__item-col')
divsother = section.find_all('div', class_='col-3 mb-3 rubricator-list__item-col d-none')

rub = {}
tenders = {}
# recordsPerPage=_10 - максимально по 100 позиций на странице

for d in divs:
	name = d.span.text.strip()
	link = f'https://zakupki.gov.ru{d.a["href"]}'
	count = d.find('div', class_='rubricator-list__item-value').text.strip()
	rub.update({name:[link, count]})
for d in divsother:
	name = d.span.text.strip()
	link = f'https://zakupki.gov.ru{d.a["href"]}'
	count = d.find('div', class_='rubricator-list__item-value').text.strip()
	rub.update({name:[link, count]})
pprint(rub)

for r in rub:
	resp = requests.get(rub.get(r)[0], verify=False)
	soup = BeautifulSoup(resp.text, 'lxml')
	rows = soup.find_all('div', class_='row no-gutters registry-entry__form mr-0')

	for row in rows:
		rowresp = requests.get(f'https://zakupki.gov.ru/{row.a["href"]}', verify=False)
		rowsoup = BeautifulSoup(resp.text, 'lxml')
		# print(rowsoup)
		break
	break

