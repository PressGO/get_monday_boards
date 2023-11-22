# get Monday.com Boards

Query monday.com boards via board ID and save as json or csv files
and upload it to object storage

Need to setup an apikey.env file in your own working directory
It should include the monday.com API_KEY="your_api_key" and the API_URL="https://api.monday.com/v2"

## Usage

query boards using MondayAPIClient class. Ensure the query template is in the template folder.

The DataHandler class manipulates MondayAPIClient objects to get tabular data from json files

To store data use the FileManager to save MondayAPIClient object boards as a specific file type in a specific folder
