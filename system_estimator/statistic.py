import pandas as pd
import numpy as np

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
    filename = "./data/" + file
    
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
    
    pdsf_filename = filename.split("/")
    
    pdsf_filename = f"{file[:file.find('_')]}_pdsf"
    pdsf.to_csv(f'./data/{pdsf_filename}.csv', index=False)
    
    return f'./data/{pdsf_filename}.csv'