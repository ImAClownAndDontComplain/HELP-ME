from .sql_api import *
import math

class DPService():
    def __init__(self):
        self.connector = SQLiteStoreConnector("sqlite:///D:/circus/ПО/ПО_4/ПО_4/database.sqlite")
        self.connector.connect()

    def get_source_files(self):
        return select_all_from_source_files(self.connector)

    def get_av_grade(self):
        avgrade = get_average_grade(self.connector)
        return avgrade[0]

    def get_data_count(self):
        count = get_data_count(self.connector)
        return count[0]



