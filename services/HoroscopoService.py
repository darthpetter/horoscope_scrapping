import requests as req
from bs4 import BeautifulSoup as BS

class HoroscopoService:
    def web_scrapping_horoscopo():
        try:
            website_url='https://www.clarin.com/horoscopo/'
            required_website=req.get(website_url)

            website_content = BS(required_website.content, "html.parser")

            horoscopo_cards=website_content.find_all('div',class_='item')

            zodiaco=list()

            for card in horoscopo_cards:
                titulo=card.find('h2')
                mensajes=card.find_all('p',class_='')
                mensajes_depurados=[]

                for elemen in mensajes:
                    mensajes_depurados.append(elemen.text)

                response={
                    'titulo':str(titulo.text).upper(),
                    'mensajes':mensajes_depurados,
                }
                zodiaco.append(response)

            return {
                'ok':True,
                'data':zodiaco,
            }
        except:
            return {
                'ok':False,
                'message':'Algo salió mal );',
            }

