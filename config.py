import os
# print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
class BaseConfig(object):
    """
    Using this class to share any default attributes with any subsequent
    classes that inherit from BaseConfig.
    """
    DEBUG = False

 
    ENV="develpoment"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

 


    BASE_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'bookstore')
 

 




class DevelopmentConfig(BaseConfig):

    DEBUG = True
    
  


    # For using SQLite3 databast
    SQLITE_DB_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'db.sqlite')
    print(SQLITE_DB_DIR)
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+SQLITE_DB_DIR
    SQLALCHEMY_ECHO = True
