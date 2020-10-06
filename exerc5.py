import requests, webbrowser, bs4
import re
from selenium import webdriver

print("Digite algo a ser buscado: ")
fraseBuscada = input()
#palavra = input(‘Insira a palavra a ser pesquisada: ‘)
#dataMax = input(‘Agora a data mais recente dos resultados: ‘)
#dataMin = input(‘A data mais antiga: ‘)
#idioma = input(‘Insira agora o idioma da pesquisa: ‘)

#mensagem pro usuário
print("Googling " + fraseBuscada + "...")

#faz a requisição passando um termo ao buscador do google
#res = requests.get('http://google.com/search?q=' + palavra + '&lr=lang_' + idioma + '&tbs=cdr:1,cd_min:' +dataMin+ 'cd_max:' + dataMax)


res = requests.get('http://google.com/search?q=' + fraseBuscada )



#verifica erros, interrompendo a execução caso ocorra problemas
res.raise_for_status()

#bs4 analisa o html da página do google retornada
soup = bs4.BeautifulSoup(res.text, features="lxml")



#seleciono os elementos com classe r no interior de uma tag a (hyperlink)
linksList = soup.select('a')
contador = 0

#Faz a busca dos links penera eles e salva os resultados uteis para minha aplicação
for i in linksList:
    if contador == 2:
        break
    else:
        a = i.get('href')
        if (a.count("img")):
            print("pulando um resultado que é imagem")
        else:
            if (a.count("wikipedia") or a.count("youtube")):
                print("Pulando wikipedia/youtube")
            else:
                if (a.count("https")):
                    a = a[7:]
                    index = 0
                    for letra in a:
                        if ("&" == letra):
                            a = a[:index]
                        index = index + 1                    
                    
                    link = requests.get(a)
                    pag = bs4.BeautifulSoup(link.text, features="lxml")
                    pag = pag.text
                    
                    contador = contador + 1
                    print(a)
                   
                    arquivo = open(str(contador) + "_site.txt", "w")
                    arquivo.write(pag)
                    arquivo.close()


print("Done.")

