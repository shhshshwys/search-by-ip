import requests
import folium
import os
import webbrowser
from pyfiglet import Figlet
from colorama import Fore

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}IP{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('query'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Провайдер{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('isp'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Организация{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('org'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Страна{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('country'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Регион{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('regionName'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Город{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('city'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}ZIP{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('zip'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Ширина{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('lat'),
            f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Долгота{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}': response.get('lon')
        }
        for k, v in data.items():
            print(f'{k} : {v}')
        isp = str(response.get('isp'))
        if isp.strip() == 'None':
            print(f'{Fore.LIGHTRED_EX}[!] {Fore.LIGHTMAGENTA_EX}Укажите настоящий IP адрес!{Fore.RESET}')
        else:
            open_html(
                lat=response.get('lat'), 
                lon=response.get('lon'),
                query=response.get('query'),
                city=response.get('city')
                )
    except requests.exceptions.ConnectionError:
        print(f'{Fore.LIGHTRED_EX}[!] {Fore.LIGHTMAGENTA_EX}Проверьте ваше интернет соединение!{Fore.RESET}')

def open_html(lat, lon, query, city):
        answer = input(f'\n{Fore.LIGHTWHITE_EX}Открыть {Fore.LIGHTGREEN_EX}.html {Fore.LIGHTWHITE_EX}файл в браузере по умолчанию? {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Y{Fore.LIGHTBLACK_EX}/{Fore.LIGHTRED_EX}N{Fore.LIGHTWHITE_EX}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}: {Fore.LIGHTYELLOW_EX}')
        if answer == 'Y':
            area = folium.Map(location=[lat, lon])
            folium.Marker([lat, lon]).add_to(area)
            file_name = f'{query}_{city}.html'
            area.save(file_name)
            webbrowser.open_new_tab(file_name)
            print(f'{Fore.LIGHTCYAN_EX}[i] {Fore.LIGHTMAGENTA_EX}Файл открыт в браузере.{Fore.RESET}')
        else:
            print(f'{Fore.LIGHTCYAN_EX}[i] {Fore.LIGHTMAGENTA_EX}Скрипт завершил работу.{Fore.RESET}')
            pass

def main():
    os.system('cls')
    preview_text = Figlet(font='slant')
    print(Fore.LIGHTBLUE_EX)
    print(preview_text.renderText('IP INFO'))
    ip = input(f'{Fore.LIGHTWHITE_EX}Введите {Fore.LIGHTGREEN_EX}IP адрес{Fore.LIGHTWHITE_EX}: {Fore.LIGHTYELLOW_EX}')
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
