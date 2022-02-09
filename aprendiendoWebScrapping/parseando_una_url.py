# Practicando parsear una URL de youtube jeje

'''
url = 'http://www.youtube.com/embed/K8L6KVGG-7o?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent'

# Mi razonamiento

url_sep = url.split('/')
url_sep.pop(3)
url_sep = '/'.join(url_sep)
url_final = url_sep.split('?')[0]
print(url_final)
'''

# El razonamiento del ejercicio

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('http://coreyms.com').text
# soup = BeautifulSoup(source, 'lxml')

# ? Con la función find podemos encontrar cosas en el texto
# article = soup.find('article')
# print(article.prettify())

# ? Vemos que nos podemos quedar con el texto de esta forma
# ? los .h2 .a es para decirle donde está lo que querés
# headline = article.h2.a.text
# print(headline)

# ! Voy a tratar de imprimir el contenido ahora

# ? Acá se muestra cómo buscar una sección con una clase en particular
# summary = article.find('div', class_='entry-content').p.text
# print(summary)

# ! Y ahora vamos a quedarnos con el link del video (que hay que parsear)

# url = article.find('iframe', class_='youtube-player')['src']

# parte_util = url.split('/')[4]

# vid_id = parte_util.split('?')[0]

# print(vid_id)

# yt_link = f'https://www.youtube.com/watch?v={vid_id}'
# print(yt_link)


# & AHORA PODEMOS APLICAR ESTO A TODOS LOS ARTÍCULOS DE LA PÁGINA!

from bs4 import BeautifulSoup
import requests
import sys

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

#! Acá metemos un cambio para que encuentre TODOS LOS ARTÍCULOS
articles = soup.find_all('article')

original_stdout = sys.stdout

with open('articulo_scrapeado.txt', 'w') as f:
    sys.stdout = f
    for article in articles:
        headline = article.h2.a.text
        print(headline)
        print('=' * len(headline), end='\n\n')

        summary = article.find('div', class_='entry-content').p.text
        print(summary, end='\n\n')

        try:
            url = article.find('iframe', class_='youtube-player')['src']
            parte_util = url.split('/')[4]
            vid_id = parte_util.split('?')[0]
            yt_link = f'https://www.youtube.com/watch?v={vid_id}'
            print('URL: ' + yt_link)
        except:
            pass

        print()
sys.stdout = original_stdout
