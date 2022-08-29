import os
from typing import List
import _csv
import csv
from services.logger import logger
import data_cleaner
import numpy as np
from elements import elements_list

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
        # logger.info(f"Opening {fpath}")
        # Using utf-8-sig to read a file will treat BOM as file info instead of a string.
        with open(fpath, newline='', encoding='utf-8-sig') as csvfile:
            reader = _csv.reader(csvfile, delimiter = delimiter, quotechar='"')
            data = [row[0] for row in reader if len(row) > 0]
        logger.info(f"Loaded {fpath} containing {len(data)} items")
        logger.info(f"first 10 items: {data[0::20]}")
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
        # 输入是最终csv文件的存储路径，和get_data_from_csv() return的结果；
        # 输出是存到csv文件里的数据，return none
        csv_reader = csv.reader(open("compositions.csv"))
        total_row = sum(1 for line in open("compositions.csv"))
        result = np.zeros((total_row, len(elements_list)), dtype=float)
        # print(result)
        count = 0
        for alloy in csv_reader:
            alloy_ratio = data_cleaner.normalize_molar_ratios(data_cleaner.clean_row(str(alloy[0]))[1])
            alloy_dic = dict(zip(data_cleaner.clean_row(str(alloy[0]))[0], alloy_ratio))
            # print(alloy_dic.keys())
            for key in alloy_dic.keys():
                result[count, elements_list.index(key)] = float(alloy_dic.get(key))
                # print(result)
            count += 1

        print(np.shape(result))

        ## Save the result(array) as the 'Parser.csv'
        err_csv = os.path.join(os.path.expanduser('.'), 'deploy', 'error.csv')

        with open("Parser.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter='，')

            for row in result:
                writer.writerow(row)
