from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://coinmania.com/news/'
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(request_site).read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 col-xxl-3')
results = []

for item in news:
    title = item.find('a', class_='post__title').get_text()
    # print('title:', title)
    href = item.a.get("href")
    # print('href:', href)
    perehod = Request(item.a.get("href"),headers={"User-Agent": "Mozilla/5.0"})
    pereshel = urlopen(perehod)
    htmls = pereshel.read()
    soups = BeautifulSoup(htmls, 'html.parser')
    desc = soups.find('meta', property="og:description", content=True)
    desc_txt = str(desc["content"])
    desc_res = desc_txt[0:170] + '...'
    # print('description:', desc_res)
    image = item.find('div', class_="post__image")
    imager = str(image["style"])
    imager_final = imager[17:imager.find(".webp")+5]
    # print(imager_final)
    results.append({'title': title, 'href': href, 'description': desc_res, 'picture': imager_final})

print(results)
