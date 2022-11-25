import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user1",
   password="abc123"
)
print("This is a dictionary. Use commands list, add, delete, quit")
#read_dict=show the dictionary
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
#add_word= add a word and translation to the dictionary
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
#delete_word= deletes a word and translation from the dictionary
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#save_dict= commits changes to the dictionary
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
#insert_word= printing some text
def insert_word(C, word, translation):
    print("This function only prints text")

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
