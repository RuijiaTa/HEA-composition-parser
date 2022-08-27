import sys
from typing import List
from csv_service import CsvReader


def parser( fpath : str, delimiter : str = ','):
    # get data from csv file
   data : List[ str ]= CsvReader.get_data_from_csv(fpath, delimiter)


if __name__ == '__main__':
    #TODO: fix access of the script args
    fpath = sys.argv[1]
    delimiter= sys.argv[2]
    parser(fpath, delimiter)
