import os
import pandas as pd
from settings import UPLOAD_DIR

def encoding(file):
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)

    try:
        df = pd.read_csv(filename)
        df.to_csv(filename, encoding='utf-8', index=False)
        return True
    except:
        pass

    try:
        df = pd.read_csv(filename, encoding='euc-kr')
        df.to_csv(filename, encoding='utf-8', index=False)
        return True
    except:
        pass

    try:
        df = pd.read_csv(filename, encoding='cp949')
        df.to_csv(filename, encoding='utf-8', index=False)
        return True
    except:
        pass

    return False


def read_csv_to_df(file):
    filename = os.path.join(UPLOAD_DIR + "/odsf/", file)
    try:
        # read odsf file
        df = pd.read_csv(filename, encoding='utf-8')
    except:
        df = pd.DataFrame()
    
    return df