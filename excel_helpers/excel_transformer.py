from exceptions.exceptions import NotImplemented


class DataTransformer:
    def __init__(self):
        self.data_frame = None

    def transform_data_types(self, column_types):
        convert_data_type = {
            'float': float,
            'int': int,
            'str': str
        }
        for column, data_type in column_types.items():
            try:
                self.data_frame[column] = self.data_frame[column].astype(convert_data_type[data_type])
            except ValueError as e:
                raise NotImplemented(f"Error transforming data type for column {column}: {e}")
        return self.data_frame
