import pandas as pd

from exceptions.exceptions import NotImplemented


class CleaningOperations:
    def remove_duplicates(self):
        self.data_frame = self.data_frame.drop_duplicates()

    def drop_na_values(self):
        self.data_frame = self.data_frame.dropna()

    def fill_na_with_mean_values(self):
        for column in self.data_frame.columns:
            if pd.api.types.is_numeric_dtype(self.data_frame[column]):
                self.data_frame[column] = self.data_frame[column].fillna(self.data_frame[column].mean())
    
    def fill_na_with_median_values(self):
        for column in self.data_frame.columns:
            if pd.api.types.is_numeric_dtype(self.data_frame[column]):
                self.data_frame[column] = self.data_frame[column].fillna(self.data_frame[column].median())


class DataCleaner(CleaningOperations):
    def __init__(self):
        self.data_frame = None

    def handle_missing_values(self, option='drop'):
        if option == 'drop':
            self.drop_na_values()
        elif option == 'mean':
            self.fill_na_with_mean_values()
        elif option == 'median':
            self.fill_na_with_median_values()
        elif option == 'remove_duplicates':
            self.remove_duplicates()
        else:
            raise NotImplemented("Invalid Option. Supported strategies: 'drop', 'mean', 'median'")
        return self.data_frame
