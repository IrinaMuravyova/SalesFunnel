import sqlite3

class Database:
    def __init__(self, db_path: str = 'clients.db'):
        self.db_path = db_path
    
    @property # взаимодействуем с подключением как со свойством
    def connection(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data=cursor.fetchall()
        connection.close()
        return data
    #TODO: сделать это асинхронно через серверную БД

# таблица пользователей
    def create_table_users(self):
        sql="""
        CREATE TABLE Users(
        id int NOT NULL,
        age_category int,
        goal int
        status int,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

# таблица возрастных категорий
    def create_table_age_categorys(self):
        sql="""
        CREATE TABLE AgeCategories(
        id int NOT NULL,
        age_category text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

# таблица целей обучения
    def create_table_goals(self):
        sql="""
        CREATE TABLE Goals(
        id int NOT NULL,
        goal text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

# таблица статусов
    def create_table_statuses(self):
        sql="""
        CREATE TABLE Statuses(
        id int NOT NULL,
        status text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)