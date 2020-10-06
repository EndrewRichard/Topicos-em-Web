import requests, bs4

res = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/3251/pinheiral-rj')
print (res.status_code)
soup = bs4.BeautifulSoup(res.text, 'html5lib')
maxTemp = soup.find('span', attrs={'id': 'max-temp-1'})
minTemp = soup.find('span', attrs={'id': 'min-temp-1'})
dia = soup.find('h1', attrs={'class': '-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5'})

dia = dia.text
maxTemp = maxTemp.text
minTemp = minTemp.text



arquivo = open("climatempo.txt", "w")

            
arquivo.write(dia)
arquivo.write(" \n MAX:")
arquivo.write(maxTemp)
arquivo.write(" \n MIN:")
arquivo.write(minTemp)
arquivo.close()

