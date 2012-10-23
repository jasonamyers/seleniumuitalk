from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

BACK_END = r'sqlite:///db/test.db'
ENGINE = create_engine(BACK_END, pool_recycle=3600)
SESSION = scoped_session(sessionmaker(bind=ENGINE))
BASE = declarative_base()