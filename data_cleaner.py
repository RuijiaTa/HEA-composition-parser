from elements import elements_list
from typing import List, double
import logging as logger

class CsvReader:
   
    #TODO : create this function
    @staticmethod
    def normalize_molar_ratios ( ratios : List[double]):
        """ 
        Normalizes molar ratios to sum up to 1

        Parameters: 
            List [double]: A list of molar ratios.
                e.g. [1, 0.5, 0.5, 1, 1]

        Returns: 
            List [double]: A normalized version of the list 
                e.g. [0.25 , 0.125, 0.125, 0.25, 0.25]
        """

    #TODO : create this function
    @staticmethod
    def clean_row (row : str) :
        # remove +/- signs

        # split string into element and molar ratio tokens 

        # check tokens in element whitelist
        
        # 
        return ""