from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://coinmania.com/news/'
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(request_site, timeout=10).read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 col-xxl-3')
results = []

for item in news:
    title_node = item.find('a', class_='post__title')
    image = item.find('div', class_="post__image")
    if not title_node or not item.a or not image:
        continue

    title = title_node.get_text(strip=True)
    # print('title:', title)
    href = item.a.get("href")
    # print('href:', href)
    perehod = Request(item.a.get("href"),headers={"User-Agent": "Mozilla/5.0"})
    pereshel = urlopen(perehod, timeout=10)
    htmls = pereshel.read()
    soups = BeautifulSoup(htmls, 'html.parser')
    desc = soups.find('meta', property="og:description", content=True)
    if not desc:
        continue
    desc_txt = str(desc["content"])
    desc_res = desc_txt[0:170] + '...'
    # print('description:', desc_res)
    imager = str(image["style"])
    imager_final = imager[17:imager.find(".webp")+5]
    # print(imager_final)
    results.append({'title': title, 'href': href, 'description': desc_res, 'picture': imager_final})

print(results)
