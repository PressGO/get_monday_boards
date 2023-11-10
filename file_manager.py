import json
import os

class FileManager:
    """Manages file operations for data storage."""
    # Define the default folder path as a class attribute
    DEFAULT_FOLDER_PATH = r'C:\Users\Juan Peng\monscript\storage'
    
    @classmethod
    def ensure_directory_exists(cls):
        if not os.path.exists(cls.DEFAULT_FOLDER_PATH):
            os.makedirs(cls.DEFAULT_FOLDER_PATH)

    @classmethod
    def save_to_json(cls, data, filename):
        cls.ensure_directory_exists()  # Make sure the directory exists
        full_path = os.path.join(cls.DEFAULT_FOLDER_PATH, filename)
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def save_to_csv(cls, dataframe, filename):
        cls.ensure_directory_exists()  # Make sure the directory exists
        full_path = os.path.join(cls.DEFAULT_FOLDER_PATH, filename)
        dataframe.to_csv(full_path, index=False)