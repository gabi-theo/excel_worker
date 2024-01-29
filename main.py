import pandas as pd

from excel_helpers.excel_aggregation import DataStatistics
from excel_helpers.excel_cleaner import DataCleaner
from excel_helpers.excel_filters import DataFilter
from excel_helpers.excel_reader_writer import ExcelHandler
from excel_helpers.excel_sorter import DataSorter
from excel_helpers.excel_transformer import DataTransformer
from excel_helpers.utils import is_valid_excel_path


class ExcelWorker(
    DataStatistics,
    DataCleaner,
    DataFilter,
    DataSorter,
    DataTransformer,
    ExcelHandler,
):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    program_running = True
    excel_worker = ExcelWorker()
    excel_path = input("Please provide your path to excel:")
    while not is_valid_excel_path(excel_path):
        print("Invalid excel path. Try again")
        excel_path = input("Please provide your path to excel:")
    excel_worker.read_excel(excel_path)
    print("Excel loaded")
    excel_worker.print_excel_header()
    print("""
        In your terminal, select your next actions:
          - "dc" -> data cleaning. This allows you to handle missing values. Valid options: 
                - drop -> Will drop empty values
                - mean  -> Will mean the empty values
                - median -> Will return the median value for empty values
                - remove_duplicates -> Will remove duplicated values
          - "df" -> data filtering. Will filter data based on given parameter and value. Valid options:
                - eq -> Will filter data equal with given value
                - gt -> Will filter data greater than given value
                - gte -> Will filter data greater or equal than given value
                - lt -> Will filter data less than given value
                - lte -> Will filter data less or equal than given value
          - "ds" -> data sorting. Will sort data based on given columns. Optional, descending and ascending parameter can be provided
          - "dt" -> data transforming. Will convert values on the column based on given value
          - "di" -> data info. Will show summary of the data
          - "sd" -> save data. Will save the new excel to provided path.
          - "q" -> quit. Will close the program
    """)
    while program_running:
        VALID_OPTIONS = ("dc", "df", "ds", "dt", "di", "sd", "q")
        try:
            option = input("Select your option: ")
            while option not in VALID_OPTIONS:
                print("Option not valid")
                option = input("Select your option: ")

            if option == "dc":
                parameter = input("Select parameter for cleaning data (drop, mean, median, remove_duplicates): ")
                excel_worker.handle_missing_values(parameter)

            elif option == "df":
                parameter = input("Select column name, condition and value for filtering. First column name, then enter condition (eq, gt, gte, lt, lte). Please enter values separated by space: ")
                column_name, condition, filter_value = parameter.split(" ") 
                excel_worker.filter_data_by_column_name(column_name=column_name, condition=condition, value=filter_value)

            elif option == "ds":
                parameter = input("Select columns to sort. If you want to include sorting order, specify the value after the columns as 'desc' or 'asc'. Please enter values separated by space: ")
                sorting_columns = parameter.split(" ")
                sorting_order = True
                if sorting_columns[-1] == "asc":
                    sorting_columns.pop(-1)
                elif sorting_columns[-1] == "desc":
                    sorting_columns.pop(-1)
                    sorting_order = False

                excel_worker.sort_data(sorting_columns, sorting_order)

            elif option == "dt":
                parameter = input("Select column and data type that you wont to convert to. Valid options for converting data: 'int', 'float', 'str'. Please enter values separated by space: ")
                column, data_type = parameter.split(" ")
                excel_worker.transform_data_types({column: data_type})

            elif option == "di":
                excel_worker.show_summary_statistics()

            elif option == "sd":
                excel_path = input("Enter path and the name of the new excel file that you want to save with modified data frame: ")
                while not is_valid_excel_path(excel_path):
                    print("Invalid excel path. Try again")
                    excel_path = input("Please provide your path to excel:")
                excel_worker.export_to_excel(output_file_path=excel_path)

            elif option == "q":
                program_running = False
                print("Exiting program....")
            excel_worker.print_excel_header()
        except Exception as e:
            print(f"Exception happened: {e}")
