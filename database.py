from sqlalchemy import create_engine, text
import os 

my_secret = os.environ['DB_CONNECTION_STRING']
db = my_secret
engine = create_engine(db, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})