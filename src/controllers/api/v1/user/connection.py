# import psycopg2
# from psycopg2.extras import RealDictCursor

# #Database Connection
# try:
#     connection = psycopg2.connect(
#         host = 'localhost',
#         user = 'postgres',
#         database = 'fitness',
#         password = 'hello',
#         cursor_factory = RealDictCursor
#     )
#     cursor = connection.cursor()
#     print("Database connect successfully")

# except Exception as error:
#     print("Database not connected")
#     print("Error =",error)