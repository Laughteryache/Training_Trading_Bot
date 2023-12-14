import psycopg2

conn = psycopg2.connect(user='postgre', password='1234')
conn.autocommit = True


class database:
    def __init__(self, name):
        self.name = name

    def create_table(self):
        with conn.cursor() as cur:
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.name}
            (id INT,
            deposit INT,
            positions TEXT)
            ;""")
            print('[INFO] TABLE CREATED SUCCESSFULLY')

    def insert_new_user(self, id):
        with conn.cursor() as cur:
            cur.execute(f"""INSERT INTO {self.name} (id, deposit, positions) 
            VALUES ({id}, {100000}, '');
            """)
            print('[INFO] USER INSERT SUCCESSFULLY')

    def get_user_info(self, id):
        with conn.cursor() as cur:
            cur.execute(f"""SELECT deposit, positions FROM {self.name} 
            WHERE id = {id};
            """)
            print('[INFO] USER INFO DROPPED')


conn.close()