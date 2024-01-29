import pandas as pd
from exceptions.exceptions import ColumnNotFound, OtherExceptions


class DataSorter:
    def __init__(self):
        self.data_frame = None

    def sort_data(
            self,
            columns: list,
            ascending: bool=True):
        try:
            for col in columns:
                if col not in self.data_frame.columns:
                    raise ColumnNotFound(f"Column '{col}' does not exist in the DataFrame.")

            self.data_frame = self.data_frame.sort_values(by=columns, ascending=ascending)
        except Exception as e:
            raise OtherExceptions(f"Exception happened on data sorting: {e}")
