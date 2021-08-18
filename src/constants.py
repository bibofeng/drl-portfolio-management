import os
DATABASE_DIR = os.path.realpath(__file__).\
    replace('pgportfolio/constants.pyc','/database/Data.db').\
    replace("pgportfolio\\constants.pyc","database\\Data.db").\
    replace('pgportfolio/constants.py','/database/Data.db').\
    replace("pgportfolio\\constants.py","database\\Data.db")

LIB_DIR = os.path.dirname(__file__)  
print("lib_dir:"+LIB_DIR)
DB_DIR = os.path.realpath(__file__)
print("db_dir"+ DB_DIR)