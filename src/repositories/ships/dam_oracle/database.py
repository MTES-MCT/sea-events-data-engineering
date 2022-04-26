from sqlalchemy.engine import create_engine

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'XXXXXXX'
PASSWORD = 'XXXXXXX'
HOST = 'cheruette.dsi.damgm.i2'
PORT = 1521
SERVICE = 'OCANI'
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

db_engine = create_engine(ENGINE_PATH_WIN_AUTH)
