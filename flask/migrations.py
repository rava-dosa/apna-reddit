import psycopg2
conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
cur = conn.cursor()
cur.execute("CREATE TABLE if not exists USER1 (user_id text PRIMARY KEY, name text, pass text, created_at timestamp, email_id text, date_of_birth date, city text, state text);")
cur.execute("CREATE TABLE if not exists contact_numbers(user_id text REFERENCES USER1(user_id),phone_no integer, primary key (user_id, phone_no));")
conn.commit()