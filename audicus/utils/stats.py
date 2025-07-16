from __future__ import absolute_import, print_function, unicode_literals

import pandas as pd
from pandas.core.series import Series

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD


class DF:
    STATUS_KEY = "status__c"

    def __init__(self, data):
        self.status_count = {
            STATUS_ACTIVE: 0,
            STATUS_CANCELLED: 0,
            STATUS_ON_HOLD: 0,
        }
        self.data = data
        self.__setup()

    def __setup(self):
        self.df = pd.DataFrame.from_dict(self.data)
        categories: Series = self.df.groupby(self.STATUS_KEY).size()
        keys = categories.index.to_list()
        values = categories.to_list()
        self.status_count = dict(zip(keys, values))

    def get_size_by_category(self, cat: str) -> Series:
        """Returns Dataframe by the category"""
        categories: Series = self.df.groupby(cat).size()

        return categories
