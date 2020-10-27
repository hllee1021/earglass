from database.connection import queryall

def get_all_samples():
   return queryall("SELECT * FROM SAMPLE")

def create_sample():
    pass
