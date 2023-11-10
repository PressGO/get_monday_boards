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

# Convert the response content into a dictionary
def main():
    # setup api varaibles
    load_dotenv("apikey.env")
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')
    headers = {"Authorization" : api_key}

    # initialise mondayAPIClient class and load query template
    client = MondayApiClient(api_url=api_url, headers=headers)
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, 'templates', 'stats.graphql')
    client.add_query_template('stats', template_path)

    # query from specific board via board id
    board_id = 5100178786
    query_items = client.load_query('stats', board_id=board_id)

    # get board data as a json file
    boards_data = client.fetch_data(query_items)
    FileManager.save_to_json(boards_data, 'stats.json')

    # get board data as a tabular csv
    items_data = client.fetch_data(query_items)
    items = items_data["data"]["boards"][0]["items"]
    processed_items = DataHandler.process_items_to_dict(items)
    df = DataHandler.convert_to_dataframe(processed_items)
    FileManager.save_to_csv(df, 'board_items.csv')

if __name__ == '__main__':
    main()