import os


def is_valid_excel_path(file_path):
    _, file_extension = os.path.splitext(file_path.lower())
    return file_extension in ['.xls', '.xlsx']
