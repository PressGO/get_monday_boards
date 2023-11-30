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
    
    @staticmethod
    def convert_from_df_to_stat(items, team):
        """Convert a stats dataframe into the dataframe format that SSSM uses for stats"""
        # calculate total work hours from indirect and direct columns
        items["Total Work (h)"] = items["Direct Service (h)"].add("Indirect Service (h)")

        # Create new column end date -  Note: monday board should already have this inside instead of creating new column
        items["End Date \n (dd/mm/yyyy)\nif applicable"] = items["Date"].copy()
        
        # Map columns from the original data to the target format
        transformed_df = items.copy()
        transformed_df.rename(columns={}) # check if columns are correctly mapped from template

        # Insert the transformed data into the target format starting from the identified row
        for index, row in transformed_df.iterrows():
            for col_num, value in enumerate(row, start=1):
                #sheet.cell(row=start_row + index, column=col_num, value=value)
                # to input team - check board id from config and use that instead
                transformed_df["S/No."] = range(1, len(items) + 1)
                transformed_df["Sport Science Team"] = team
                transformed_df["Start Date (dd/mm/yyyy)"] = items["Date"]
                transformed_df["End Date \n (dd/mm/yyyy)\nif applicable"] = None  # Not available in original data
                transformed_df["Sports"] = items["Sport/s"]
                transformed_df["No. of Athletes"] = None  # Not available in original data
                transformed_df["Name of Athlete (non spex)/ Team"] = items["Name of Athlete/s"]
                transformed_df["Name of Spex Scholar\n"] = None  # Not available in original data
                transformed_df["Location"] = items["Location"]
                transformed_df["Description"] = items["Name"]
                transformed_df["Staff Initial"] = items["Staff"]
                transformed_df["Direct Service"] = items["Direct Service (h)"]
                transformed_df["Indirect Service"] = items["Indirect Service (h)"]
                transformed_df["Total Hrs"] = items["Total Work (h)"]
        
        return transformed_df
    