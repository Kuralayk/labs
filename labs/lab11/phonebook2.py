import psycopg2

def connect():
    return psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password="npg_qsSHdPejW1i5",
        host="ep-sparkling-rain-a4aj55uv-pooler.us-east-1.aws.neon.tech"
    )

def search_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
            return cur.fetchall()

def insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))

def insert_many_users(names, phones):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s, %s, %s);", (names, phones, None))
            conn.commit()

def get_page(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
            return cur.fetchall()

def delete_user(identifier):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user(%s);", (identifier,))

if __name__ == "__main__":
    print(search_by_pattern("Ali"))

    insert_or_update_user("Ali", "87010000000")

    names = ['Aru', 'Zhan']
    phones = ['87020000000', 'invalid']
    print(insert_many_users(names, phones))

    print(get_page(3, 0))

    delete_user("87020000000")


