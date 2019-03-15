import psycopg2
conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
cur = conn.cursor()
cur.execute("CREATE TABLE if not exists USER1 (user_id text PRIMARY KEY, name text, pass text, created_at timestamp, email_id text, date_of_birth date, city text, state text);")
cur.execute("CREATE TABLE if not exists contact_numbers(user_id text REFERENCES USER1(user_id),phone_no integer, primary key (user_id, phone_no));")
cur.execute("CREATE table if not exists subreddit (name text primary key, subreddit_created_at timestamp, user_id text REFERENCES user1(user_id));")
cur.execute("CREATE table if not exists post (post_id text primary key, content text, post_created_at timestamp, user_id text REFERENCES user1(user_id), subreddit_name text REFERENCES subreddit(name));")
cur.execute("CREATE table if not exists post_liked(user_id text references user1(user_id), post_id text references post(post_id));")
cur.execute("CREATE table if not exists post_disliked(user_id text references user1(user_id), post_id text references post(post_id));")
cur.execute("CREATE table if not exists comment(comment_id text primary key, user_id text references user1(user_id), comment_content text, created_at timestamp, parent_id text, post_id text references post(post_id));")
cur.execute("CREATE table if not exists cookie(user_id text references user1(user_id), cookie text, primary key(user_id, cookie));")
conn.commit()

