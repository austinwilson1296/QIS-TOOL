from sqlalchemy import create_engine, text
import os 
from sqlalchemy.sql.selectable import Values

my_secret = os.environ['db_connection_string']
db = my_secret
engine = create_engine(db, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

def add_repair(start_time, end_time, sku_number, repair_codes):

      query = text("INSERT INTO repairjobs (start_time, end_time, sku_number, repair_codes) VALUES (:start_time, :end_time, :sku_number, :repair_codes)")

      values = {
          'start_time': start_time,
          'end_time': end_time,
          'sku_number': sku_number,
          'repair_codes': repair_codes
      }
      with engine.connect() as conn:
          conn.execute(query, values)