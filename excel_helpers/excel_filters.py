import pandas as pd

from exceptions.exceptions import ColumnNotFound, FilterError


class FilterConditions:
    def _gt(self, column, value):
        return lambda x: x[column] > value
    
    def _gte(self, column, value):
        return lambda x: x[column] >= value
    
    def _lt(self, column, value):
        return lambda x: x[column] < value
    
    def _lte(self, column, value):
        return lambda x: x[column] <= value
    
    def _eq(self, column, value):
        return lambda x: x[column] == value


class DataFilter(FilterConditions):
    def __init__(self):
        self.data_frame = None

    def filter_data_by_column_name(self, column_name, condition, value):
        filter_conditions = {
            "eq": self._eq,
            "gt": self._gt,
            "gte": self._gte,
            "lt": self._lt,
            "lte": self._lte,
        }
        if column_name not in self.data_frame.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

        if filter_conditions.get(condition):
            condition_function = filter_conditions.get(condition)(column_name, int(value))
            self.data_frame = self.data_frame[self.data_frame.apply(condition_function, axis=1)]
        else:
            raise FilterError(f"Filter condition - {condition} not implemented")
