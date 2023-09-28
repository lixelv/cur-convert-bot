import sqlite3


class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.do("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state INTEGER DEFAULT 0,
    data TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
    );""")

    def do(self, query: str, values=()) -> None:
        self.cursor.execute(query.replace('%s', '?'), values)
        self.connect.commit()

    def read(self, query: str, values=(), one=False) -> tuple:
        self.cursor.execute(query.replace('%s', '?'), values)
        return self.cursor.fetchall() if not one else self.cursor.fetchone()

    def user_exists(self, user_id: int) -> bool:
        return bool(self.read('SELECT id FROM user WHERE id = ?;', (user_id,)))

    def add_user(self, user_id: int, user_name: str):
        self.do('INSERT INTO user(id, name) VALUES(?, ?);', (user_id, user_name))

    def set_state(self, user_id: int, state: int) -> None:
        self.do('UPDATE user SET state = ? WHERE id = ?;', (state, user_id))

    def state(self, user_id: int) -> bool:
        return self.read('SELECT state FROM user WHERE id = ?;', (user_id,), one=True)[0]

    def set_data(self, user_id: int, data: str) -> None:
        self.do('UPDATE user SET data = ? WHERE id = ?;', (data, user_id))

    def get_data(self, user_id: int) -> str:
        return self.read('SELECT data FROM user WHERE id = ?;', (user_id,), one=True)[0]

