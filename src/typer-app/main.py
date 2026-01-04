import sqlite3
from pathlib import Path
import typer 

db_path = Path("table.sql")
app = typer.Typer()

def get_conn():
    """Establish connection"""
    return sqlite3.connect(db_path)

    
def init_table():
    """The first command is to initialize sql table."""

    sql_command = """
    CREATE TABLE IF NOT EXISTS typer_table (
        UserID INT Primary Key,
        Name TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    """
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(sql_command)
    conn.commit()
    conn.close()




@app.command()
def init():
    """
    Initialize table
    """
    try:
        init_table()
        typer.secho("Command 1 satisfied")
    except sqlite3.Error:
        typer.secho("Command 1 failed")
        raise typer.Exit(code=1)
    

if __name__ == "__main__":
    app()
