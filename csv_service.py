import os
from typing import List
import _csv
import logging as logger

class CsvService:
    @staticmethod
    def get_data_from_csv(fpath: str, delimiter = ',') -> List[ str ]:
     '''   
        Retrieves alloy composition data from a .csv file given as input.

        Parameters:
            fpath: absolute path to the file
            delimiter

        Returns:
            List with elements as each row in the .csv
        '''

        if not os.path.exists(fpath):
            raise OSError(filename=fpath)
        logger.info(f"Opening {fpath}")
        # Using utf-8-sig to read a file will treat BOM as file info. instead of a string.
        with open(fpath, newline='', encoding='utf-8-sig') as csvfile:
            reader = _csv.reader(csvfile, delimiter, quotechar='"')
            data = []
            for row in reader:
                # skip empty rows
                if(len(row) > 0):
                    data.append(row)
        logger.info(f"Loaded {fpath} containing {len(data)} items")
        return data
    
    #TODO : create this function
    @staticmethod
    def write_data_to_csv(fpath: str,  data : List [ str ]):
        '''
        Writes alloy composition data to a given file.

        Parameters:
            fpath: relative / absolute path to the output file
            data: 53-element vector with molar ratios of each element [0, 0.8, 0, 0, 0.2, ...]

        Returns:
            None
        '''
        return None



    