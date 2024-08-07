
import requests
from bs4 import BeautifulSoup

def main():
  URL = 'https://www.bbc.com/weather/964420'
  page = requests.get(URL)
  soup = BeautifulSoup(page.text, 'html5lib')

  print("Below is some information scraped from a website that has some information regarding todays weather:")

  s = soup.find_all('span', class_ = 'wr-value--temperature--c')
  print("Today's high temp: ")
  s1 = s[0].text
  print(s1)
  print("Today's low temp: ")
  s2 = s[1].text
  print(s2)

if __name__ == '__main__':
  main()
  
 
  
