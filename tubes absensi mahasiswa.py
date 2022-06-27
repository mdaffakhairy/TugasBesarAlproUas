#TUBES ALPRO
#M Daffa Khairy

#setup
import sqlite3
from tkinter import *
from tkinter import ttk

#setup untuk judul diatas
root = Tk()
root.title("Absensi Mahasiswa")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Absensi Mahasiswa"

#fungsi untuk tuple tempat memasukkan data
def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

#fungsi untuk memasukkan data
def insert( nim, nama, absen, kehadiran):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(absensinim TEXT, absensinama TEXT, absensiabsen TEXT, absensikehadiran TEXT)""")

    cursor.execute("INSERT INTO inventory VALUES ('" + str(nim) + "','" + str(nama) + "','" + str(absen) + "','" + str(kehadiran) + "')")
    conn.commit()

#fungsi untuk menghapus data 
def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(absensinim TEXT, absensinama TEXT, absensiabsen TEXT, absensikehadiran TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE absensinim = '" + str(data) + "'")
    conn.commit()

#fungsi untuk memperbarui data
def update(nim, nama, absen, kehadiran,  idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(absensinim TEXT, absensinama TEXT, absensiabsen TEXT, absensikehadiran TEXT)""")

    cursor.execute("UPDATE inventory SET absensinim = '" + str(nim) + "', absensinama = '" + str(nama) + "', absensiabsen = '" + str(absen) + "', absensikehadiran = '" + str(kehadiran) + "' WHERE absensinim='"+str(idName)+"'")
    conn.commit()

#fungsi untuk membaca data
def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(absensinim TEXT, absensinama TEXT, absensiabsen TEXT, absensikehadiran TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results

#fungsi dalam pengkondisian dan error handling ketika akan memasukkan data
def insert_data():
    absensinim = str(entrynim.get())
    absensinama = str(entrynama.get())
    absensiabsen = str(entryabsen.get())
    absensikehadiran = str(entrykehadiran.get())
    try:
        if absensinim == "" or absensinim == " ":
         print("Error Inserting Nim")
        if absensinama == "" or absensinama == " ":
         print("Error Inserting Nama")
        if absensiabsen == "" or absensiabsen == " ":
         print("Error Inserting Absen")
        if absensikehadiran == "" or absensikehadiran == " ":
         print("Error Inserting Kehadiran")
    except:
        TypeError
        print("input salah")
    else:
        insert(str(absensinim), str(absensinama), str(absensiabsen), str(absensikehadiran))

#looping untuk digunakan terus-menerus
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

#fungsi untuk menghapus data
def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

#fungsi untuk memperbaharui data
def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entrynim.get(), entrynama.get(), entryabsen.get(), entrykehadiran.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

#desain
titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

nimLabel = Label(root, text="NIM", font=('Arial bold', 15))
namaLabel = Label(root, text="Nama", font=('Arial bold', 15))
absenLabel = Label(root, text="Absen", font=('Arial bold', 15))
kehadiranLabel = Label(root, text="Kehadiran", font=('Arial bold', 15))
nimLabel.grid(row=1, column=0, padx=10, pady=10)
namaLabel.grid(row=2, column=0, padx=10, pady=10)
absenLabel.grid(row=3, column=0, padx=10, pady=10)
kehadiranLabel.grid(row=4, column=0, padx=10, pady=10)

entrynim = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrynama = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryabsen = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrykehadiran = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrynim.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entrynama.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryabsen.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entrykehadiran.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("NIM", "Nama", "Absen", "Kehadiran")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("NIM", anchor=W, width=200)
my_tree.column("Nama", anchor=W, width=200)
my_tree.column("Absen", anchor=W, width=150)
my_tree.column("Kehadiran", anchor=W, width=150)
my_tree.heading("NIM", text="NIM", anchor=W)
my_tree.heading("Nama", text="Nama", anchor=W)
my_tree.heading("Absen", text="Absen", anchor=W)
my_tree.heading("Kehadiran", text="Kehadiran", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
#eksekusi
root.mainloop()