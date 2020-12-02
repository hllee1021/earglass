import os
import json
import pandas as pd
import numpy as np
import math
from settings import UPLOAD_DIR
from .statistic import *
import services


def transform_encoding(file):
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)

    try:
        df = pd.read_csv(filename)
        df.to_csv(filename, encoding='utf-8')
        return True
    except:
        pass

    try:
        df = pd.read_csv(filename, encoding='euc-kr')
        df.to_csv(filename, encoding='utf-8')
        return True
    except:
        pass

    try:
        df = pd.read_csv(filename, encoding='cp949')
        df.to_csv(filename, encoding='utf-8')
        return True
    except:
        pass

    return False


def to_pdsf(file):
    """
    when odsf is submitted, then call this method to change odsf to pdsf.
    input : filename is odsf
    output : pdsf locate
    """
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)
    
    try:
        # read odsf file
        odsf = pd.read_csv(filename, encoding='utf-8')
    except:
        return "no file"
    
    # statistic analysis
    statistic_data = null_count(odsf)
    duplicate_info = duplicate_tuple(odsf)
    
    # create dataframe of pdsf
    pdsf_statistic_schema = list(odsf.columns) + ['total tuple','duplicate tuple', 'duplicate rate']
    statistic_data['total tuple'] = duplicate_info['total_tuple_num']
    statistic_data['duplicate tuple'] = duplicate_info['duplicate_num']
    statistic_data['duplicate rate'] = duplicate_info['duplicate_rate']
    
    # map value to list, to make df
    for key in statistic_data.keys():
        tmp = list()
        tmp.append(statistic_data[key])
        statistic_data[key] = tmp
        
    pdsf_statistic_df = pd.DataFrame(statistic_data)
    
    
    
    n_df = pdsf_statistic_df.add([np.nan for i in range(pdsf_statistic_df.shape[1])])
    h_df = pd.DataFrame(dict(zip(odsf.columns, list(map(lambda x : [x],odsf.columns)))))
    
    # combine dataframe to pdsf
    pdsf = pd.concat([pdsf_statistic_df, n_df, h_df, odsf]).reset_index(drop=True)
    
    pdsf_filename = os.path.join(UPLOAD_DIR + "/pdsf/", file)
    pdsf.to_csv(pdsf_filename, index=False, encoding='utf-8')
    
    return pdsf_filename
