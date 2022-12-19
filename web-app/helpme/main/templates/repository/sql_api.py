from .connector import StoreConnector
from .sqliteconnector import SQLiteStoreConnector
from pandas import DataFrame, Series
from datetime import datetime
from typing import List


'''def get_grade(connector: StoreConnector):
    cols = ['SCHOLARSHIP', 'STUDY_HRS', 'READ_FREQ', 'READ_FREQ_SCI', 'IMPACT', 'ATTEND', 'PREP_STUDY', 'PREP_EXAM',
            'NOTES', 'LISTENS', 'LIKES_DISCUSS', 'CUML_GPA']
    row = [4, 5, 2, 2, 1, 1, 2, 2, 3, 3, 3, 5]
    query = "SELECT * FROM processed_data"
    database = connector.execute(query).fetchall()
    data = DataFrame([row], columns = cols)
    dataset = DataFrame(columns = cols)
    for row in database:
        database[row]'''

def get_data_count(connector: StoreConnector):
    query = f'SELECT COUNT(*) AS count FROM processed_data'
    result = connector.execute(query).fetchone()
    return result

def get_average_grade(connector: StoreConnector):
    query = f'SELECT AVG(GRADE) AS avg FROM processed_data'
    result = connector.execute(query).fetchone()
    return result

def select_all_from_source_files(connector: StoreConnector) -> List[tuple]:
    """ Вывод списка обработанных файлов с сортировкой по дате в порядке возрастания (DESCENDING) """
    query = f'SELECT * FROM source_files ORDER BY processed ASC'
    result = connector.execute(query).fetchall()
    return result


def select_rows_from_processed_data(connector: StoreConnector, source_file: int, offset: int = None, limit: int = 10) -> List[tuple]:
    """ Выборка строк из таблицы с обработанными данными.
        offset - смещение строк при выборке.
        limit - количество строк в выбоке.
        Например, при запросе: SELECT * FROM processed_data WHERE source_file = {source_file} LIMIT 20,10
        будет выбрано 10 строк, начиная с 21-ой.
    """
    result = []
    if limit is None or offset is None:
        result = connector.execute(f"SELECT * FROM processed_data WHERE source_file = {source_file}").fetchall()
    else:
        result = connector.execute(f"SELECT * FROM processed_data WHERE source_file = {source_file} "
                                   f"LIMIT {offset*limit},{limit}").fetchall()
    return result

