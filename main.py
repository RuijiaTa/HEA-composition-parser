import sys
from typing import List
from services.csv_service import CsvService
from services.logger import logger


def parser( fpath : str, delimiter : str = ','):
    # get data from csv file
   data : List[ str ]= CsvService.get_data_from_csv(fpath, delimiter)


if __name__ == '__main__':
    #TODO: fix access of the script args
    try:
        fpath = sys.argv[1]
        delimiter= sys.argv[2]
        logger.info(f"entered parameters: \n fpath: {fpath}, \n delimiter: {delimiter}")
    except IndexError as e:
        error_message : str = "must call script with arguments: <filepath> <csv-delimiter>"
        message  = {e: error_message}
        raise Exception(message)
    parser(fpath, delimiter)
