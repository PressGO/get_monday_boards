import pandas as pd

class DataHandler:
    """Processes data and converts it into different formats."""

    @staticmethod
    def process_items_to_dict(items):
        """Convert API items to a list of dictionaries."""
        processed_items = []
        for item in items:
            item_data = {"name": item["name"]}
            for column in item["column_values"]:
                item_data[column["title"]] = column["text"]
            processed_items.append(item_data)
        return processed_items

    @staticmethod
    def convert_to_dataframe(items):
        """Convert a list of dictionaries to a pandas DataFrame."""
        return pd.DataFrame(items)