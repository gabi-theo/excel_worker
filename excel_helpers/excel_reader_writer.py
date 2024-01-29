from exceptions.exceptions import ReadWriteException

import pandas as pd


class ExcelHandler:
    def __init__(self):
        self.data_frame = None

    def export_to_excel(self, output_file_path, sheet_name='Sheet1', index=False):
        try:
            self.data_frame.to_excel(output_file_path, sheet_name=sheet_name, index=index)
            print(f"DataFrame exported to Excel file: {output_file_path}")
        except Exception as e:
            raise ReadWriteException(f"Error exporting DataFrame to Excel: {e}")

    def read_excel(self, file_path, sheet_name=0):
        try:
            self.data_frame = pd.read_excel(file_path, sheet_name=sheet_name)
        except Exception as e:
            raise ReadWriteException(f"Error exporting DataFrame to Excel: {e}")

    def print_excel_header(self):
        print(self.data_frame.head())
