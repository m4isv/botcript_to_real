import requests

def bitcoin_to_real(bitcoin_amount):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "brl"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        bitcoin_price_brl = data["bitcoin"]["brl"]
        real_amount = bitcoin_amount * bitcoin_price_brl
        return real_amount
    else:
        return None

# Exemplo de uso
#bitcoin_amount = 0.00028360
#real_amount = bitcoin_to_real(bitcoin_amount)

def dogecoin_to_real(dogecoin_amount):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "dogecoin",
        "vs_currencies": "brl"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        bitcoin_price_brl = data["dogecoin"]["brl"]
        real_amount = dogecoin_amount * bitcoin_price_brl
        return real_amount
    else:
        return None


# Exemplo de uso
#dogecoin_amount = 52.00998989
#real_amount = dogecoin_to_real(dogecoin_amount)
#print(real_amount)


