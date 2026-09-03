import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "student_predictions.db"
)


def create_table():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hours_studied REAL,
            attendance REAL,
            previous_scores REAL,
            predicted_score REAL
        )
    """)

    connection.commit()
    connection.close()


def save_prediction(
    hours_studied,
    attendance,
    previous_scores,
    predicted_score
):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (hours_studied, attendance, previous_scores, predicted_score)
        VALUES (?, ?, ?, ?)
    """, (
        hours_studied,
        attendance,
        previous_scores,
        predicted_score
    ))

    connection.commit()
    connection.close()


def get_predictions():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM predictions
        ORDER BY id DESC
    """)

    data = cursor.fetchall()
    connection.close()

    return data


if __name__ == "__main__":
    create_table()
    print("Database created successfully!")
def delete_predictions():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM predictions")

    connection.commit()
    connection.close()    