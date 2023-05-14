from services.HoroscopoService import HoroscopoService

def main():
    continuar=True
    responseWeb=HoroscopoService.web_scrapping_horoscopo()
    if(responseWeb['ok']==False):
        print(responseWeb['message'])
        continuar=False

    
    while continuar==True:
        dataZodiacal=responseWeb['data']
        print('----------------------------------------------------------------')
        print('\n')
        print('HOLA BIENVENIDO')
        print('HOROSCOPO DEL DIA')
        print('\n')
        signo_usuario=str(input('¿Podrías decirme tu signo zodiacal? ')).upper()
        index = next((i for i, signo in enumerate(dataZodiacal) if signo['titulo'] == signo_usuario), -1)
        print('\n')
        if(index==-1):
            print('No pudimos identificar el signo que escribiste );')
        else:
            mensajes=dataZodiacal[index]['mensajes']
            print('********************************')
            for msj in mensajes:
                print(msj)
            print('********************************')  
        print('\n')
        print('¿Deseas continuar o te gustaría consultar otra vez?')
        desea_continuar=str(input('Pulsa C para continuar ')).upper()
        if(desea_continuar!='C'):
            continuar=False


if __name__ == "__main__":
    main()