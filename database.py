from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://zaga4d0tpprdnoo9bwid:pscale_pw_rTwEtrzKtgZxKgNsJ3T4ySAt2gCateZ431SsQE5Wc0e@aws.connect.psdb.cloud/shop_tool'
engine = create_engine(db_connection_string)