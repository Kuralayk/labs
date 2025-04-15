import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="1234"
)

cur = conn.cursor()

# Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()


# Загрузка из CSV
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                        (row['name'], row['phone']))
    conn.commit()
    print("✅ Данные из CSV загружены.")


# Ввод с консоли
def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Добавлено.")


# Обновление данных
def update_entry():
    old_name = input("Введите существующее имя: ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый номер: ")
    cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s",
                (new_name, new_phone, old_name))
    conn.commit()
    print("✅ Обновлено.")


# Поиск
def search():
    value = input("Введите имя или номер для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    rows = cur.fetchall()
    if rows:
        print("🔍 Найдено:")
        for row in rows:
            print(row)
    else:
        print("❌ Ничего не найдено.")


# Удаление
def delete_entry():
    value = input("Введите имя или номер для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print("🗑️ Удалено.")


# Меню
def menu():
    while True:
        print("\n📱 PhoneBook Menu:")
        print("1. Загрузить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить запись")
        print("4. Найти запись")
        print("5. Удалить запись")
        print("6. Выйти")
        choice = input("Выбор: ")

        if choice == '1':
            insert_from_csv('contacts.csv')
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            search()
        elif choice == '5':
            delete_entry()
        elif choice == '6':
            break
        else:
            print("❗ Неверный выбор")

menu()

cur.close()
conn.close()
