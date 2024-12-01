from EnergyParser.outage_info_parser import OutageInfoParser
from EnergyParser.energy_site_parser import EnergySiteParser
from EnergyParser.region import Region


class ParserManager:
    def __init__(self, parser: OutageInfoParser):
        self.__parser = parser

    async def get_outage_list(self, region: Region, index: str):
        energy_data = await self.__parser.parse_outage_list(region, index)
        return energy_data

    def change_parser(self, new_parser: OutageInfoParser):
        self.__parser = new_parser


if __name__ == "__main__":
    pm = ParserManager(EnergySiteParser())
    energy_list = pm.get_outage_list(Region.SUMY, '4')
    print(energy_list)
