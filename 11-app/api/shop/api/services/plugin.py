from typing import List
from abc import abstractmethod, ABC
from shop.api.model import Shop


class Plugin(ABC):
    @abstractmethod
    def name(self) -> str:
        """
        Retrieves the name of the data source plugin.

        :return: The name of the data source plugin.
        :rtype: str
        """
        pass

    @abstractmethod
    def identifier(self) -> str:
        """
        Retrieves a unique identifier for the data source plugin.

        :return: The unique identifier of the data source plugin.
        :rtype: str
        """
        pass


class DataSourcePlugin(Plugin):
    """
    An abstraction representing a plugin for loading shop data from a specific data source.
    """

    @abstractmethod
    def load(self, **kwargs) -> List[Shop]:
        """
        Loads data from the data source and returns it as a list of `Shop` objects.

        :param kwargs: Arbitrary keyword arguments for customization or filtering of the data loading process.
        :type kwargs: dict
        :return: A list of `Shop` objects loaded from the data source.
        :rtype: List[Shop]
        """
        pass
