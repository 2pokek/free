import requests
from bs4 import BeautifulSoup
from proxy_config import login, password, proxy

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

proxies = {
    'https': f'http://{login}:{password}@{proxy}'
}


def get_data(url):
    response = requests.get(url=url, headers=headers)
    print(response)


def main():
    get_data(url='https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm')


if __name__ == '__main__':
    main()
