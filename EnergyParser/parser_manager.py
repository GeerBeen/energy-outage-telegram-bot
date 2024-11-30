from EnergyParser.outage_info_parser import OutageInfoParser
from EnergyParser.energy_site_parser import EnergySiteParser
from EnergyParser.region import Region


class ParserManager:
    def __init__(self, parser: OutageInfoParser):
        self.__parser = parser

    def get_outage_list(self, region: Region, index: str):
        raw_data = self.__parser.request_html_page_and_get_soup(region, index)
        scales_list = self.__parser.get_div_list(raw_data)
        energy_data = self.__parser.get_outages_list(scales_list)
        return energy_data

    def change_parser(self, new_parser: OutageInfoParser):
        self.__parser = new_parser


if __name__ == "__main__":
    pm = ParserManager(EnergySiteParser())
    energy_list = pm.get_outage_list(Region.SUMY,'4')
    print(energy_list)
