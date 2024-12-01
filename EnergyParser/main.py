import asyncio
from EnergyParser.energy_site_parser import EnergySiteParser
from EnergyParser.region import Region
from EnergyParser.parser_manager import ParserManager


async def main():
    pm = ParserManager(EnergySiteParser())
    energy_data = await pm.get_outage_list(Region.SUMY, '4')  # Використовуємо await
    print(energy_data)


if __name__ == "__main__":
    asyncio.run(main())
