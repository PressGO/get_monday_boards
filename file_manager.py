import json
import os

class FileManager:
    """Manages file operations for data storage."""
    @staticmethod
    def ensure_directory_exists(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    staticmethod
    def save_to_json(data, filename, directory_path):
        FileManager.ensure_directory_exists(directory_path)  # Make sure the directory exists
        full_path = os.path.join(directory_path, filename)
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_to_csv(dataframe, filename, directory_path):
        FileManager.ensure_directory_exists(directory_path)
        full_path = os.path.join(directory_path, filename)
        dataframe.to_csv(full_path, index=False)