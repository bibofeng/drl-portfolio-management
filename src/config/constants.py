import os
DATABASE_DIR = os.path.realpath(__file__).\
    replace('pgportfolio/constants.pyc','/database/Data.db').\
    replace("pgportfolio\\constants.pyc","database\\Data.db").\
    replace('pgportfolio/constants.py','/database/Data.db').\
    replace("pgportfolio\\constants.py","database\\Data.db")

CFG_LIB_DIR = os.path.dirname(__file__)  
print("in config lib_dir:"+CFG_LIB_DIR)
CFG_DB_DIR = os.path.realpath(__file__)
print("in config db_dir"+ CFG_DB_DIR)