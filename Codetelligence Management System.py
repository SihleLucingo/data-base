import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Management System"

photo1 = PhotoImage(file="sihle.png")
Label (root, image=photo1, bg="black") .grid(row=0, column=10, pady=20, padx=(20,20) )


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( Name, D_O_B, Stream, Sex):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemName TEXT, itemD_O_B TEXT, itemStream TEXT, itemSex TEXT)""")

    cursor.execute("INSERT INTO inventory VALUES ('" + str(Name) + "','" + str(D_O_B) + "','" + str(Stream) + "','" + str(Sex) + "')")
    conn.commit()


def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemName TEXT, itemD_O_B TEXT, itemStream TEXT, itemSex TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()


def update(Name, D_O_B, Stream, Sex, idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemName TEXT, itemD_O_B TEXT, itemStream TEXT, itemSex TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = '" + str(Name) + "', itemName = '" + str(D_O_B) + "', itemPrice = '" + str(Stream) + "', itemQuantity = '" + str(Sex) + "'WHERE itemId='"+str(idName)+"'")
    conn.commit()


def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemName TEXT, itemD_O_B TEXT, itemStream TEXT, itemSex TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results


def insert_data():
    itemName = str(entryName.get())
    itemD_O_B = str(entryD_O_B.get())
    itemStream = str(entryStream.get())
    itemSex = str(entrySex.get())
    if itemName == "" or itemName == " ":
        print("Error Inserting Nme")
    if itemD_O_B == "" or itemD_O_B == " ":
        print("Error Inserting D_O_B")
    if itemStream == "" or itemStream == " ":
        print("Error Inserting Stream")
    if itemSex == "" or itemSex == " ":
        print("Error Inserting Sex")
    else:
        insert(str(itemName), str(itemD_O_B), str(itemStream), str(itemSex))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryName.get(), entryD_O_B.get(), entryStream.get(), entrySex.get() ,update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)


titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

NameLabel = Label(root, text="Name", font=('Arial bold', 15))
D_O_BLabel = Label(root, text="D_O_B", font=('Arial bold', 15))
StreamLabel = Label(root, text="Stream", font=('Arial bold', 15))
SexLabel = Label(root, text="Sex", font=('Arial bold', 15))
NameLabel.grid(row=1, column=0, padx=10, pady=10)
D_O_BLabel.grid(row=2, column=0, padx=10, pady=10)
StreamLabel.grid(row=3, column=0, padx=10, pady=10)
SexLabel.grid(row=4, column=0, padx=10, pady=10)

entryName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryD_O_B = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryStream = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrySex = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryName.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryD_O_B.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryStream.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entrySex.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=7, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=7, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=delete_data)
buttonDelete.grid(row=7, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("Name", "D_O_B", "Stream", "Sex")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=100)
my_tree.column("D_O_B", anchor=W, width=200)
my_tree.column("Stream", anchor=W, width=150)
my_tree.column("Sex", anchor=W, width=150)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("D_O_B", text="D_O_B", anchor=W)
my_tree.heading("Stream", text="Stream", anchor=W)
my_tree.heading("Sex", text="Sex", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()
