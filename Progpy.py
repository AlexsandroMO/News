import requests
from bs4 import BeautifulSoup
import pandas as pd

def news_all():
  search_url = 'https://g1.globo.com/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('a.gui-color-hover')

  list_news = []
  
  for itens in product_elemt:
    list_news.append([itens.text, itens.get('href'), 'G1'])

  #-----------------------------------
  search_url = 'https://www1.folha.uol.com.br/ultimas-noticias/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('div.c-headline__content')

  for a in range(len(product_elemt)):
    A = product_elemt[a].select('h2.c-headline__title')[0].text
    B = product_elemt[a].select('a')[0].get('href')
    list_news.append([A, B, 'FSP'])

  #-----------------------------------
  def name(link):
    search_url = link
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    response_object = requests.get(search_url, headers=headers)

    search_soup = BeautifulSoup(response_object.text, features='html.parser')
    product_elemt = search_soup.select('title')

    return product_elemt[0].text

  search_url = 'https://odia.ig.com.br'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('div.share-teaser')

  for i in range(len(product_elemt)):
    if i < 10:
      for a in product_elemt[i].select('div.twitter'):
        #print(a.get('data-url'))
        link = a.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

      for b in product_elemt[i].select('div.share-teaser'):
        #print(b.get('data-url'))
        link = b.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

      for c in product_elemt[i].select  ('div.whatsapp'):
        #print(c.get('data-url'))
        link = c.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

  #-----------------------------------
  search_url = 'https://www.r7.com/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('a.r7-flex-hat__description')

  for itens in product_elemt:
    list_news.append([itens.get('title'), itens.get('href'), 'R7'])

  return list_news

def news_g1():
  search_url = 'https://g1.globo.com/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('a.gui-color-hover')

  list_news = []
  for itens in product_elemt:
    list_news.append([itens.text, itens.get('href'), 'G1'])

  return list_news

def news_r7():
  search_url = 'https://www.r7.com/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('a.r7-flex-hat__description')

  list_news = []
  for itens in product_elemt:
    list_news.append([itens.get('title'), itens.get('href'), 'R7'])

  return list_news

def news_fsp():
  search_url = 'https://www1.folha.uol.com.br/ultimas-noticias/'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('div.c-headline__content')

  list_news = []
  for a in range(len(product_elemt)):
    A = product_elemt[a].select('h2.c-headline__title')[0].text
    B = product_elemt[a].select('a')[0].get('href')
    list_news.append([A, B, 'FSP'])

  return list_news


def all_resume(news):
  df = pd.DataFrame(data=news, columns=['News','Link','Tipo'])

  df_g1 = df[df['Tipo'] == 'G1'].head(3)
  df_fsp = df[df['Tipo'] == 'FSP'].head(3)
  df_dia = df[df['Tipo'] == 'DIA'].head(3)
  df_r7 = df[df['Tipo'] == 'R7'].head(3)

  x = 0
  for a in df_fsp.index:
    df_fsp.rename(index={a:x}, inplace=True)
    x += 1

  y = 0
  for a in df_dia.index:
    df_dia.rename(index={a:y}, inplace=True)
    y += 1

  z = 0
  for a in df_r7.index:
    df_r7.rename(index={a:z}, inplace=True)
    z += 1

  list_news = []
  for a in range(len(df_g1)):
    list_news.append([df_g1['News'].loc[a],df_g1['Link'].loc[a],df_g1['Tipo'].loc[a]])
    list_news.append([df_fsp['News'].loc[a],df_fsp['Link'].loc[a],df_fsp['Tipo'].loc[a]])
    list_news.append([df_dia['News'].loc[a],df_dia['Link'].loc[a],df_dia['Tipo'].loc[a]])
    list_news.append([df_r7['News'].loc[a],df_r7['Link'].loc[a],df_r7['Tipo'].loc[a]])

  return list_news

def news_dia():
  def name(link):
    search_url = link
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    response_object = requests.get(search_url, headers=headers)

    search_soup = BeautifulSoup(response_object.text, features='html.parser')
    product_elemt = search_soup.select('title')

    return product_elemt[0].text

  search_url = 'https://odia.ig.com.br'

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response_object = requests.get(search_url, headers=headers)

  search_soup = BeautifulSoup(response_object.text, features='html.parser')
  product_elemt = search_soup.select('div.share-teaser')

  list_news = []

  for i in range(len(product_elemt)):
    if i < 10:
      for a in product_elemt[i].select('div.twitter'):
        #print(a.get('data-url'))
        link = a.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

      for b in product_elemt[i].select('div.share-teaser'):
        #print(b.get('data-url'))
        link = b.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

      for c in product_elemt[i].select  ('div.whatsapp'):
        #print(c.get('data-url'))
        link = c.get('data-url')
        name(link)
        list_news.append([name(link), a.get('data-url'), 'DIA'])

  return list_news