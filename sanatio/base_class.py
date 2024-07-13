import os
import json


class BaseValidator:
    """Base validator class for validating the data"""

    def isvalidString(self, value: str) -> bool:
        """Check if the string is valid or not"""
        return isinstance(value, str) and value != ''

    def isvalidNumber(self, value: int) -> bool:
        """Check if the number is valid or not"""
        return isinstance(value, (int, float))

    def isvalidBoolean(self, value) -> bool:
        """Check if the value is boolean or not"""
        return isinstance(value, bool)

    def removeSpaces(self, value) -> str:
        """Remove spaces from string"""
        return value.replace(" ", "") if self.isvalidString(value) else None
    
    def isFileExists(self, file_path: str) -> bool:
        """Check if the file exists or not"""
        return os.path.exists(file_path)
    
    def read_file(self, 
                  file_path: str, 
                  split_lines: bool = False, 
                  unique: bool = False, 
                  is_json: bool = False,
                  sep: str = '\n',
                  mode: str = 'r') -> list:
        """Read the file content"""
        if self.isFileExists(file_path):
            if is_json:
                return self.read_json(file_path)
            
            with open(file_path, mode) as file:
                data = file.read()
                if split_lines and unique:
                    return list(set(data.split(sep)))
                return data
        return None
        
    def read_json(self, file_path: str) -> dict:
        """Read the json file content"""
        if self.isFileExists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        return {}

    def write_file(self, 
                   file_path: str, 
                   data: str, 
                   mode: str = 'w', 
                   sep: str = '') -> bool:
        """Write the data to the file"""
        with open(file_path, mode) as file:
            for line in data:
                file.write(line + sep)
        return True

    def write_json(self, file_path: str, data: dict) -> bool:
        """Write the data to the json file"""
        with open(file_path, 'w') as file:
            json.dump(data, file)
        return True

    def boolConversion(self, value: str, output=[True, False]) -> bool:
        """Convert the string to boolean
        
        input: 'true', 'yes', 'y', '1', 't' -> True
               'false', 'no', 'n', '0', 'f' -> False
        
        output: True or False
                1 or 0
                y or n
                t or f
        """
        if str(value).lower() in ['true', 'yes', 'y', '1', 't']:
            return output[0]
        elif str(value).lower() in ['false', 'no', 'n', '0', 'f']:
            return output[1]
        return None
