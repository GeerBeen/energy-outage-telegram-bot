import asyncio
from EnergyParser.energy_site_parser import EnergySiteParser
from EnergyParser.region import Region


async def main():
    parser = EnergySiteParser()
    data = await parser.request_html_page_and_get_soup(Region.SUMY, '4')
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
