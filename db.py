from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pymysql
pymysql.install_as_MySQLdb()
connectionString="mysql+mysqldb://root:India12#$@localhost/alchemydb2"
engine = create_engine(connectionString,echo=False)#echo True will print on screen
session = Session(engine)