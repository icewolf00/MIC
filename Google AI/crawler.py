import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

def get_link(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'html.parser')
	csvfile = open('link.csv', 'a')
	# print("title,link", file = csvfile)
	for i in soup.find_all('h2'):
		try:
			title = i.find('a').text
			title = title.replace('\n', '')
			link = i.find('a')['href']
			link = link.replace('\n', '')
			csvfile.write(title + "," + link + '\n')
			# print(link)
			# print(title + "," + link, file = csvfile)
		except:
			pass
	csvfile.close()

def get_text(link):
	html = requests.get(link).text
	soup = BeautifulSoup(html, 'html.parser')
	title = soup.find('h2').find('a').text.strip('\n')
	title = title.replace('/', ' ')
	title = title.replace(':', '')
	text = soup.body.text
	text = text.replace('&#8220;', '"')
	text = text.replace('&#8221;', '"')
	text = text.replace('&#8217;', "'")
	text = text.replace('&#8212;', "-")
	text = text.replace('&amp;', "&")
	text = text.replace('&nbsp;', '')
	text = text.replace('\n', '')
	start = text.index('<span', 0)
	end = text.index('<span', start+1)
	text = text[start:end]
	while True:
		try:
			left = text.index('<', 0)
			right = text.index('>', 0)
			tag = text[left:right+1]
			text = text.replace(tag, '')
		except:
			break
	path = 'article/' + title + '.txt'
	textfile = open(path, 'w')
	textfile.write(title)
	textfile.write(text.encode("utf8").decode("cp950", "ignore"))
	textfile.close()

def main():
	csvfile = open('link.csv', 'w')
	csvfile.write("title,link\n")
	csvfile.close()
	for i in range(1, 6):
		url = 'https://ai.googleblog.com/2018/0' + str(i)
		get_link(url)
	link_file = pd.read_csv('link.csv',encoding='cp1252')
	link_list = link_file['link']
	for i in link_list.values:
		get_text(i)

if __name__ == '__main__':
	main()