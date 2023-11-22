# Standard library import
import requests
import json
import os
from dotenv import load_dotenv

# Third party import
import pandas as pd

# Local app import
from api_client import MondayApiClient
from data_handler import DataHandler
from file_manager import FileManager

# Load configuration from JSON
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def main():
    # Load environment variables
    load_dotenv("apikey.env")
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')
    headers = {"Authorization": api_key}

    # Initialize MondayApiClient
    monday_client = MondayApiClient(api_url, headers)

    # Load config.json
    config = load_config('config.json')

 # Iterate over each board configuration
    for board_config in config['boards']:
        board_id = board_config['board_id']
        query_template_identifier = board_config['query_template']
        output_path = board_config['output_path']

        # Construct the path to the query template file
        template_file_path = f"templates/{query_template_identifier}.graphql"

        # Add and load query template
        monday_client.add_query_template(query_template_identifier, template_file_path)
        query = monday_client.load_query(query_template_identifier, board_id=board_id)

        # Fetch data
        board_data = monday_client.fetch_data(query)

        # Process data
        items = board_data["data"]["boards"][0]["items"]
        processed_items = DataHandler.process_items_to_dict(items)
        data_frame = DataHandler.convert_to_dataframe(processed_items)

        # Construct filename for CSV
        csv_filename = f"{board_id}.csv"
        json_filename = f"{board_id}.json"

        # Save to CSV in the specified output path
        FileManager.save_to_csv(data_frame, csv_filename, output_path)
        FileManager.save_to_json(board_data, json_filename, output_path)
        # # Check if data was retrieved
        # if not board_data:
        #     print(f"No data retrieved for board ID {board_config['board_id']}")
        #     continue  # Skip to the next board if no data

        # # Process data
        # items = board_data.get("data", {}).get("items", [])
        # if not items:
        #     print(f"No items to process for board ID {board_config['board_id']}")
        #     continue  # Skip to the next board if no items

        # processed_items = DataHandler.process_items_to_dict(items)
        # data_frame = DataHandler.convert_to_dataframe(processed_items)

        # if data_frame.empty:
        #     print(f"Data frame is empty for board ID {board_config['board_id']}")
        #     continue  # Skip to the next board if DataFrame is empty

        # # Construct filename for CSV
        # csv_filename = f"{board_config['board_id']}.csv"

        # # Save to CSV
        # try:
        #     FileManager.save_to_csv(data_frame, csv_filename, board_config['output_path'])
        #     print(f"Data saved to {os.path.join(board_config['output_path'], csv_filename)}")
        # except Exception as e:
        #     print(f"Failed to save data for board ID {board_config['board_id']}: {e}")

if __name__ == '__main__':
    main()