import psycopg2
import select
import subprocess

def listen_for_new_rentals():
    conn = psycopg2.connect("dbname=dvdrental user=postgres password=password host=localhost")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("LISTEN new_rental;")
    print("Listening for new rental inserts...")

    while True:
        if select.select([conn], [], [], 5) == ([], [], []):
            continue
        else:
            conn.poll()
            while conn.notifies:
                notify = conn.notifies.pop(0)
                print(f"New rental inserted! ID = {notify.payload}")
                subprocess.run(["python3", "data_pipeline.py"])

listen_for_new_rentals()