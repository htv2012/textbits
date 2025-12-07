import sqlite3
import pathlib


# Hard code for now
# TODO: Create dir if needed
db_path = pathlib.Path("~/.local/share/textbits/textbits.sqlite3")

def ensure_data(path):
    if path.exists():
        return
    with sqlite3.connect(path) as conn:
        conn.execute("create table bits (id integer primary key autoincrement, name text, content text)")

def create(name: str, content: str) -> int:
    cursor = conn.execute(
        "insert into bits (name, content) values (?, ?)",
        (name, content),
    )
    return cursor.lastrowid


ensure_data(db_path)
conn = sqlite3.connect(db_path)

