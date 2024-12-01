from EnergyParser.outage_info_parser import OutageInfoParser
from bs4 import BeautifulSoup
import requests
import fake_useragent
from EnergyParser.outage_state import OutageStatus
from EnergyParser.region import Region
from EnergyParser.file_reader import load_region_data

SUFFIX_URL = '/cherga/'
FILE_PATH = 'regions.json'


class EnergySiteParser(OutageInfoParser):
    def request_html_page_and_get_soup(self, region: Region, index: str):
        user = fake_useragent.UserAgent().random
        header = {'user-agent': user}

        link = load_region_data(FILE_PATH)[region.value]['url'] + SUFFIX_URL + index
        response = requests.get(link, headers=header)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"Запит завершився з помилкою: {response.status_code}")
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_div_list(self, soup):
        data_div = soup.find('div', class_='scale_hours new_scale')
        scales_list = data_div.find_all('div', class_='scale_hours_el')
        return scales_list

    def get_outages_list(self, scales_list):
        energy_list = list()
        for scale in scales_list:
            if scale.find('span', class_='hour_status hour_active'):
                energy_list.append(OutageStatus.OFF)
            elif scale.find('span', class_='hour_status hour_active_to'):
                energy_list.append(OutageStatus.FIRST_HALF_OFF)
            elif scale.find('span', class_='hour_status'):
                energy_list.append(OutageStatus.ON)
            else:
                raise ValueError('Can`t find hour status!')
        if len(energy_list) != 24:
            raise ValueError("Num of hours in energy list != 24")
        return energy_list

    def parse_outage_list(self, region: Region, index: str):
        raw_data = self.request_html_page_and_get_soup(region, index)
        scales_list = self.get_div_list(raw_data)
        energy_data = self.get_outages_list(scales_list)
        return energy_data


if __name__ == "__main__":
    sp = EnergySiteParser()
    energy_data = sp.parse_outage_list(Region.SUMY, '4')
    print(energy_data)
