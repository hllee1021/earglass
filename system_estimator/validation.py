import os
import pandas as pd
import numpy as np
import math
from settings import UPLOAD_DIR
from .statistic import *


def validate_odsf_schema(odst_id, file):
    """
    Check validate of file schema
    """
    pass

def validate_odsf_data(file, MNR, MDR):
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
        null_ratio = null / duplicate_info['total_tuple_num']
        if null_ratio > MNR/100:
            null_info[col] = False
        else:
            null_info[col] = True
    
    # calculate duplicate ratio
    if duplicate_info['duplicate_rate'] > MDR/100:
        null_info['duplicate_ratio'] = False
    else:
        null_info['duplicate_ratio'] = True
    
    return null_info