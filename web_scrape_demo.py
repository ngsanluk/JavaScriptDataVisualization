import requests
from bs4 import BeautifulSoup

url = "http://localhost:5500/index.html"
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

webpage_request = requests.get(url, headers)
soup = BeautifulSoup(webpage_request.content, 'html.parser')


#print(soup.prettify())

# Retrieve DOM element by attribute name
# print("Page Title Tag", soup.title)
# print("Page Title Text", soup.title.text)
print("\n")

# Retrieve by HTML id
dom_element = soup.find(id='page-heading')

# Retrieve by CSS class name
# dom_element = soup.find_all(class_='featured')

# Retrieve by HTML tag name
# dom_element = soup.find_all('a')


# CSS Selector
# dom_element = soup.select('div a')

print(dom_element)
