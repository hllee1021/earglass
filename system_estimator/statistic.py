import os
import pandas as pd
import numpy as np
import math
from settings import UPLOAD_DIR


def null_count(df):
    total_row = len(df.index)
    col_null = dict()
    for col in df.columns:
        col_null[col] = total_row - df[col].count()
    return col_null

def duplicate_tuple(df):
    total_tuple_num = len(df.index)
    tmp = set()
    for k in range(df.shape[0]):
        tmp.add(tuple(df.iloc[k,:]))
    isol_tuple_num = len(tmp)
    duplicate_rate = 1 - (isol_tuple_num / total_tuple_num)
    return duplicate_rate

def to_pdsf(file):
    """
    when odsf is submitted, then call this method to change odsf to pdsf.
    input : filename is odsf
    output : pdsf locate
    """
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)
    
    try:
        # read odsf file
        odsf = pd.read_csv(filename)
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
    
    
    
    n_df = s_df.add([np.nan for i in range(s_df.shape[1])])
    h_df = pd.DataFrame(dict(zip(odsf.columns, list(map(lambda x : [x],odsf.columns)))))
    
    # combine dataframe to pdsf
    pdsf = pd.concat([pdsf_statistic_df, n_df, h_df, odsf]).reset_index(drop=True)
    
    pdsf_filename = os.path.join(UPLOAD_DIR + "/pdsf/", file)
    pdsf.to_csv(pdsf_filename, index=False)
    
    return pdsf_filename


def system_score(file):
    """
    calculate system score of given file.
    input : filename is odsf
    output : system score
    """
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)
    
    try:
        # read odsf file
        odsf = pd.read_csv(filename)
    except:
        return "no file"
    
    score_info = dict()
    # statistic analysis
    null_info = null_count(odsf)
    duplicate_info = duplicate_tuple(odsf)
      
    score_info['total_tuple_score'] = math.log2(duplicate_info['total_tuple_num'])*(7.5)*(30/100)
    score_info['duplicate_tuple_score'] = (1 - duplicate_info['duplicate_rate'])*(30)
    
    null_score_list = []
    for col in null_info.keys():
        tmp = 1 - (null_info[col] / duplicate_info['total_tuple_num'])
        null_score_list.append(tmp)
    
    score_info['col_null_score'] = (sum(null_score_list)/len(null_score_list))*(40)
    
    score_info['sys_score'] = score_info['total_tuple_score'] + score_info['duplicate_tuple_score'] + score_info['col_null_score']
    
    return score_info

def check_validate(file, MNR, MDR):
    """
    Check validate of odsf file's duplicate tuple
    input : filename is odsf, MaxNullRatioPerColumn, MaxDuplicatedRowRatio
    output : boolean
    """
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)
    
    try:
        # read odsf file
        odsf = pd.read_csv(filename)
    except:
        return "no file"
    
    # statistic analysis
    null_info = null_count(odsf)
    duplicate_info = duplicate_tuple(odsf)
    
    # calculate null ratio
    for col, null in null_info.items():
        null_ratio = null/duplicate_info['total_tuple_num']
        if null_ratio > MNR:
            null_info[col] = False
        else:
            null_info[col] = True
    
    # calculate duplicate ratio
    if duplicate_info['duplicate_rate'] > MDR:
        null_info['duplicate_ratio'] = False
    else:
        null_info['duplicate_ratio'] = True
    
    return null_info