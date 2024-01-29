from exceptions.exceptions import AggregationException


class DataStatistics:
    def __init__(self):
        self.data_frame = None

    def show_summary_statistics(self):
        try:
            numeric_columns = self.data_frame.select_dtypes(include=['number'])

            summary_stats = {
                'mean': numeric_columns.mean(),
                'median': numeric_columns.median(),
                'min': numeric_columns.min(),
                'max': numeric_columns.max(),
                'std': numeric_columns.std()
            }
            print(summary_stats)
        except Exception as e:
            raise AggregationException(f"Error calculating summary statistics: {e}")
