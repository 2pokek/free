import requests
import csv
from datetime import datetime
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
    cur_date= datetime.now().strftime('%m_%d_%Y')
    # response = requests.get(url=url, headers=headers, proxies=proxies)
    # print(response)

    with open(file='index.html') as file:
        src=file.read()

    soup = BeautifulSoup(src , 'lxml')
    table = soup.find('table', id='ro5xgenergy')

    data_th = table.find('thead').find_all('tr')[-1].find_all('th')

    table_headers = ['Area']
    for dth in data_th:
        dth = dth.text.strip()
        # print(dth)
        table_headers.append(dth)

    with open(file=f'data_{cur_date}.csv',mode='w') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                table_headers
            )
        )

    tbody_trs= table.find('tbody').find_all('tr')

    data = []
    for tr in tbody_trs:
        area = tr.find('th').text.strip()

        data_by_month = tr.find_all('td')

        data = [area]
        for dbm in data_by_month:
            if dbm.find('a'):
                area_data=dbm.find('a').get('href')
            elif dbm.find('span'):
                area_data=dbm.find('span').text.strip()
            else:
                area_data = 'None'

            data.append(area_data)

        with open(file=f'data_{cur_date}.csv', mode='a') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    data
                )
            )
        return 'Done'
def main():
    get_data(url='https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm')


if __name__ == '__main__':
    main()
