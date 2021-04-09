import sqlite3
from sqlite3 import Error


def create_connection():
    conn = sqlite3.connect(
        r"F:\Onedrive - Mapúa University\Mapua\CPE 3RD YEAR\2ND TERM\CPE106L\Project\cov.db")
    c = conn.cursor()
    c.execute("INSERT INTO cov_tracker VALUES (1, 'Doroteo', 'Adrian', 'Las Pinas', '09275588445', 'Caloocan' )")
    conn.commit()
    conn.close()


create_connection()
