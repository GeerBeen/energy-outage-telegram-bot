from abc import ABC, abstractmethod
from EnergyParser.region import Region


class OutageInfoParser(ABC):
    @abstractmethod
    def request_html_page_and_get_soup(self, region: Region, index: str):
        """Отримання HTML даних із сайту та створення soup."""
        pass

    @abstractmethod
    def get_div_list(self, soup):
        """Обробка отриманих даних і створення списку div'ів клітинок відключень."""
        pass

    @abstractmethod
    def get_outages_list(self, div_list):  #
        """Повернення даних у вигляді списку елементів перелічень."""
        pass

