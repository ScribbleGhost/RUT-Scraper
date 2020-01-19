import requests,time,csv
from bs4 import BeautifulSoup

def scrape():

	with open ('results.csv', 'w', encoding='utf-8-sig', newline='') as f:
		writer = csv.writer(f, delimiter=';')
		
		page = 0
		page_has_data = True

		while page_has_data:
			base_url = 'https://RUT.org/forum/'
			r = requests.get('https://RUT.org/forum/viewforum.php?f=1715&', params=dict(start=page))
			soup = BeautifulSoup(r.text, 'html.parser')

			print(f'---------Scraping Page: {page}---------', end=';', sep=';')
			print(soup.find('title').text)

			if len(soup.findAll("a", {"class": "torTopic"})) == 0:
				page_has_data = False
				print('---------Done Scraping---------')

			for release in soup.find_all("a", {"class": "torTopic"}):
				LINK = base_url + release.get('href')
				TITLE = release.text
				writer.writerow([LINK,TITLE])

			page +=50

			time.sleep(2)

if __name__ == '__main__':
	scrape()
