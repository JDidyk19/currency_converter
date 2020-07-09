import requests

def currency():
    URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(URL).json()

    data = { currency[0]: currency[1] for currency in enumerate(response) }

    print(' ', 'Купівля', 'Продаж')
    print(data[0]["ccy"], format(float(data[0]['buy']), ".2f"), format(float(data[0]['sale'])))
    print(data[1]["ccy"], format(float(data[1]['buy']), ".2f"), format(float(data[1]['sale'])))
    print()
    from_currency = (input('З Валюти: '))
    to_currency = (input('До Валюти: '))
    amount = float(input('Кількість: '))

    def usd_uah():

        if from_currency == 'UAH' and to_currency == 'USD':
            base = 'usd'
            amount_out = amount / float(data[0]['sale'])

        elif from_currency == 'USD' and to_currency == 'UAH':
            base = 'uah'
            amount_out = amount * float(data[0]['buy'])

        print('На виході ', format(amount_out, ',.2f'), base)

    def eur_uah():

        if from_currency == 'UAH' and to_currency == 'EUR':
            base = 'eur'
            amount_out = amount / float(data[1]['sale'])

        elif from_currency == 'EUR' and to_currency == 'UAH':
            base = 'uah'
            amount_out = amount * float(data[1]['buy'])

        print('На виході ', format(amount_out, ',.2f'), base)

    def usd_usd():

        if from_currency == 'USD' and to_currency == 'USD':
            base = 'usd'
            amount_out = amount * (float(data[3]['sale']) / 10000)

        print('На виході ', format(amount_out, ',.2f'), base)


    if from_currency == 'UAH' and to_currency == 'USD' or from_currency == 'USD' and to_currency == 'UAH':
        return usd_uah()

    elif from_currency == 'UAH' and to_currency == 'EUR' or from_currency == 'EUR' and to_currency == 'UAH':
        return eur_uah()

    elif from_currency == 'USD' and to_currency == 'USD':
        return usd_usd()
    else:
        print('Немає даних')

currency()