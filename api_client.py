import requests
import os

class MondayApiClient:
    """Handles communication with the Monday.com API."""

    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers
        self.query_templates = {}
        #print(f"API URL set to: {self.api_url}")  # Debug print

    # might remove add_query if not being used
    def add_query_template(self, identifier, template_path):
        """Adds a new query template from a file."""
        with open(template_path, 'r') as file:
            self.query_templates[identifier] = file.read()
            
    def load_query(self, identifier, **kwargs):
        # Assuming you have a method to load the file content into a string
        query_template_content = self.read_query_template(identifier)
        
        # If using f-string directly in the class method:
        return query_template_content.format(**kwargs)

    def fetch_data(self, query):
        """Fetch data from the API given a GraphQL query."""
        # print("Sending query to API:", query)  # This will print the query to the console
        response = requests.post(url=self.api_url, json={'query': query}, headers=self.headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
    
    def read_query_template(self, identifier):
        # Your logic to locate and read the template file
        current_dir = os.path.dirname(__file__)
        template_path = os.path.join(current_dir, 'templates', f'{identifier}.graphql')
        with open(template_path, 'r') as file:
            return file.read()