"""
Parsing fish prices from www.mercadamadrid.es
"""
import requests
from bs4 import BeautifulSoup
import random
from datetime import date


def fishes():
    date_actual = str(date.today().day) + '-' + str(date.today().month) + '-' + str(date.today().year)
    date_minus = str(date.today().day-5) + '-' + str(date.today().month) + '-' + str(date.today().year)
    try:
        choices = ['SALMON', 'BACALAO', 'LUBINA', 'GAMBA', 'CALAMAR', 'BONITO', 'ALMEJA']
        response = requests.post('http://www.mercamadrid.es/wp-admin/admin-ajax.php?', data={
            'action': 'mercamadrir_filter_products',
            'market': 'PESCADOS',
            'product': random.choice(choices),
            'from': date_minus,
            'to': date_actual
        })

        soup = BeautifulSoup(response.text, 'lxml')
        tables = soup.find_all('tr')

        pescados = {}

        counter = 1
        for table in tables:
            test = table.find_all('td')
            if test and len(test) > 1:
                tabla_to_add = []
                for td in test:
                    tabla_to_add.append(td.text)
                pescados[counter] = tabla_to_add
                counter += 1

        pesca = pescados[1]
        text = ('El pescado más fresco está en Madrid:\n\n'
                '🐟: {}\n'
                '⚖️: {}\n'
                '🌐: {}\n'
                '💲⬆: {} €\Kg\n'
                '💲⬇: {} €\Kg\n'
                '💲🔁: {} €\Kg\n'
                '❄️: {:3.2f}% fresco'.format(pesca[0], pesca[1], pesca[2], pesca[4], pesca[5], pesca[6],
                                       random.uniform(99.00, 100)))
    except Exception as error:
        print(error)
        text = 'El pescado más fresco <b>NO</b> está en Madrid, lo siento.'

    return text
