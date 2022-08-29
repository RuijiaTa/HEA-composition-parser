from elements import elements_list
from typing import List
import logging as logger
import re

class CsvReader:

    #TODO : create this function
    @staticmethod
    def normalize_molar_ratios ( ratios : List[float]) ->List[float]:
        """ 
        Normalizes molar ratios to sum up to 1

        Parameters: 
            List [double]: A list of molar ratios.
                e.g. [1, 0.5, 0.5, 1, 1]

        Returns: 
            List [double]: A normalized version of the list 
                e.g. [0.25 , 0.125, 0.125, 0.25, 0.25]
        """
        normalized_ratios = list()
        ele_sum = sum(ratios)
        for ele in ratios:
            ele = float(ele / ele_sum)
            normalized_ratios.append(ele)
        return normalized_ratios



    #TODO : create this function
    @staticmethod
    def clean_row (row : str) :
        # remove +/- signs

        # split string into element and molar ratio tokens

        # check tokens in element whitelist

        #

        #First clean the data which is totally incorrect format((FeCrNiCo)Al0.75Cu0.25 + 10 vol.% TiC, 18Ni(200) maraging steel ) manually,
        #Then in terms of the alloys(Ag0.3+Cu1+Mn3), use the clearn_row function
        #Turn [Ag0.3+Cu2+Mn0.8+C3] to {'Ag': '0.3', 'Cu': '2', 'Mn': '0.8', 'C': '3'}

        result_ele = list()
        s = list(''.join(ch for ch in row if ch.isalpha()))
        # print(s)
        for i in range(len(s) - 1):
            if s[i].isupper() and s[i + 1].islower():
                element = str(s[i] + s[i + 1])
                result_ele.append(element)
            if s[i].isupper() and s[i + 1].isupper():
                element = str(s[i])
                result_ele.append(element)
        if len(s) != 0:
            if s[-1].isupper():
                element = str(s[-1])
                result_ele.append(element)
        # print("Elements: "+str(result_ele))

        row_list = list(row)
        for i in range(len(row_list) - 1):
            if row_list[i].islower() and row_list[i + 1].isupper():
                row_list.insert(i + 1, str(1))
            if row_list[i].isupper() and row_list[i + 1].isupper():
                row_list.insert(i + 1, str(1))
        if row_list[-1].isalpha():
            row_list.append(str(1))
            # print("New row: "+ "".join(row_list))
        result_num = re.findall(r'-?\d+\.?\d*e?-?\d*?', "".join(row_list))
        result__num = list()
        for i in result_num:
            float_ratio = float(i)
            result__num.append(float_ratio)
            # print("Ratios: " + str(result_num))
            # print("Dictionary Format: " + str(ele_dic))
        # print("Element：" + str(result_ele))
        # print("Content" + str(result_num))
        # print("---------------------------")

        return result_ele, result__num