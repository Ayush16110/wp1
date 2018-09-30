from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from lucky.credentials import WIKI_DB_STRING

Base = declarative_base()

_engine = create_engine(WIKI_DB_STRING)
Session = sessionmaker(bind=_engine)
