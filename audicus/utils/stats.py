from __future__ import absolute_import, print_function, unicode_literals
import pandas as pd


class DF:
    def __init__(self, data):
        self.data = data
        self.__setup()

    def __setup(self):
        self.df = pd.DataFrame.from_dict(self.data)

    def get_size_by_category(self, cat: str):
        """Returns Dataframe by the category"""
        return self.df.groupby(cat).size()
