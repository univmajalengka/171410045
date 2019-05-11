from tkinter import *
from tkinter import messagebox as ms
import tkinter.messagebox
import sqlite3
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk

# Session untuk menampilkan
produk_id = []
nma_brg = []
hrga_brg = []
jumlh_brg = []
jumlh_byr = []


class Utama():
    with sqlite3.connect('dbkom.db') as db:
        c = db.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
    db.commit()
    db.close()
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    # Fungsi Login
    def login(self):
        # Koneksi ke DB
        with sqlite3.connect('dbkom.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result4 = c.fetchall()
        if result4:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Login Berhasil'
            self.head['pady'] = 150
            root5 = Toplevel(self.master)
            jndl_baru = Application1(root5)
            root.after(2000, Application1)
        else:
            ms.showerror('Duhh!', 'Username Tidak Ditemukan.')

    def new_user(self):
        with sqlite3.connect('dbkom.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username sudah digunakan')
        else:
            ms.showinfo('Sukses!', 'Akun Berhasil dibuatkan')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()


    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 15), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=1, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=1, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=0, bg='greenyellow', activebackground='lightgray',
               activeforeground='black', fg='black', font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Buat Akun Baru ', bd=0, bg='palegreen', activebackground='lightgray',
               activeforeground='black', fg='black', font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Simpan', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Pergi ke Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)

    def jendelabaru(self):
        root5 = Toplevel(self.master)
        jndl_baru = Application1(root5)

class LihatBarang:
    db_name = 'dbkom.db'
    # Tampilan utama dari class Lihat Barang
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Tabel Barang")
        self.master.resizable(False, False)
        frame = LabelFrame(self.master, text= "Input Barang")
        frame.grid(row=0, column=1)
        Label (frame, text="Kode Barang: ").grid(row=1, column=2)
        self.kdbrg = Entry(frame)
        self.kdbrg.grid(row=1, column=3)
        Label(frame, text="Nama Barang: ").grid(row=2, column=2)
        self.nmbrg = Entry(frame)
        self.nmbrg.grid(row=2, column=3)
        Label(frame, text="Harga Barang: ").grid(row=3, column=2)
        self.hrgbrg = Entry(frame)
        self.hrgbrg.grid(row=3, column=3)
        Label(frame, text="Stok Barang: ").grid(row=4, column=2)
        self.stokbrg = Entry(frame)
        self.stokbrg.grid(row=4, column=3)

        ttk.Button (frame, text="Tambah Barang", command=self.tambahkanbrg).grid(row=1, column=4)
        ttk.Button(frame, text="Hapus Data", command= self.hapusdt).grid(row=8, column=1)
        ttk.Button(frame, text="Update Data", command=self.updatedb).grid(row=8, column=2)

        self.pesan = Label(frame, text='', fg='red')
        self.pesan.grid(row=5, column=5)

        self.tree = ttk.Treeview(frame, height=10, column=("column1", "column2", "column3", "column4"),show='headings')
        self.tree.grid(row=100, column=0, columnspan=50)
        self.tree.heading('#1', text='Kode Barang')
        self.tree.column('#1', anchor='center', width=100)
        self.tree.heading('#2', text='Nama Barang')
        self.tree.column('#2', anchor='center', width=120)
        self.tree.heading('#3', text='Harga Barang')
        self.tree.column('#3', anchor='center', width=120)
        self.tree.heading('#4', text='Stok Barang')
        self.tree.column('#4', anchor='center', width=80)

        self.viewing_records()
    # Koneksi database
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
    # Menampilkan data dari tabel data_brg
    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT kode_brg, nm_brg, hrg_brg, stok FROM data_brg ORDER BY kode_brg ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
           self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))

    # Validasi untuk menghindari dummy pada tabel data_brg
    def validasi(self):
        return len (self.nmbrg.get()) != 0 and len (self.stokbrg.get()) != 0 and len (self.hrgbrg.get()) != 0 and len (self.kdbrg.get()) != 0
    # Menambahkan data ke dalam tabel data_brg
    def tambahkanbrg(self):
        if self.validasi():
            query = 'INSERT INTO data_brg VALUES (?, ?, ?, ?)'
            parameters = (self.kdbrg.get(), self.nmbrg.get(), self.hrgbrg.get(), self.stokbrg.get())
            self.run_query (query, parameters)
            self.pesan['text'] = '{} Berhasil Ditambahkan'.format(self.nmbrg.get())
            self.kdbrg.delete(0, END)
            self.nmbrg.delete(0, END)
            self.stokbrg.delete(0, END)
            self.hrgbrg.delete(0, END)

            self.viewing_records()
        else:
            self.viewing_records()
    # Menghapus data dari tabel data_brg
    def hapusdt(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        for selected_item in self.tree.selection():
            cur.execute("DELETE FROM data_brg WHERE kode_brg=?", (self.tree.set(selected_item, '#1'),))
            conn.commit()
            self.pesan['text'] = '{} Telah dihapus'.format(self.nmbrg.get())
            self.tree.delete(selected_item)
        conn.close()
    # Update data pada tabel barang
    def updatedb(self):
        self.pesan ['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.pesan['text'] = 'Pilih data yang akan diubah'
            return
        name = self.tree.item(self.tree.selection())['text']
        kd_brg = self.tree.item(self.tree.selection()) ['values'][0]
        nma_brg = self.tree.item(self.tree.selection())['values'][1]
        hrga_brg = self.tree.item(self.tree.selection())['values'][2]
        stoklama = self.tree.item(self.tree.selection())['values'][3]


        self.updtdbbrg = Toplevel()
        self.updtdbbrg.title = ('Edit Data Barang')
        self.updtdbbrg.resizable(False, False)
        self.updtdbbrg.geometry("300x200")
        frame2 = LabelFrame(self.updtdbbrg, text='Update Data Barang')
        frame2.grid(row=0, column=0, columnspan=3, pady=0)

        self.kod_brg = Label(frame2, text='Kode Barang: ').grid(row=2, column=0)
        self.k_brg = Text(frame2, height=1, width=10)
        self.k_brg.config(font=("consolas", 12), undo=True, wrap='word')
        self.k_brg.insert(END, kd_brg)
        self.k_brg.grid(row=2, column=2, columnspan=2, sticky=W + E)

        self.nam_brg = Label(frame2, text='Nama Barang: ').grid(row=4, column=0)

        self.n_brg = Text(frame2, height=1, width=10)
        self.n_brg.config(font=("consolas", 12), undo=True, wrap='word')
        self.n_brg.insert(END, nma_brg)
        self.n_brg.grid(row=4, column=2, columnspan=2, sticky=W + E)

        self.har_brg = Label(frame2, text='Harga Barang: ').grid(row=6, column=0)

        self.h_brg = Text(frame2, height=1, width=10)
        self.h_brg.config(font=("consolas", 12), undo=True, wrap='word')
        self.h_brg.insert(END, hrga_brg)
        self.h_brg.grid(row=6, column=2, columnspan=2, sticky=W + E)

        self.st_brg = Label(frame2, text='Stok Barang: ').grid(row=8, column=0)

        self.s_brg = Text(frame2, height=1, width=10)
        self.s_brg.config(font=("consolas", 12), undo=True, wrap='word')
        self.s_brg.insert(END, stoklama)
        self.s_brg.grid(row=8, column=2, columnspan=2, sticky=W + E)

        ttk.Button(frame2, text='Update', command=self.simpanedit).grid(row=10, column=2, sticky=W + E)

        self.updtdbbrg.mainloop()

    def simpanedit(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        self.u1 = self.k_brg.get(1.0, END)
        self.u2 = self.n_brg.get(1.0, END)
        self.u3 = self.h_brg.get(1.0, END)
        self.u4 = self.s_brg.get(1.0, END)
        query = "UPDATE data_brg SET nm_brg=?, hrg_brg=?, stok=? WHERE kode_brg=?"
        cur.execute(query, (self.u2, self.u3, self.u4, self.u1))
        conn.commit()
        self.updtdbbrg.destroy()
        self.pesan['text'] = 'Sukses di ubah'
        self.viewing_records()


class LihatPelanggan:
    db_name = 'dbkom.db'
    # Tampilan utama dari class lihat pelanggan
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Tabel Pelanggan")
        self.master.resizable(False, False)
        frame = LabelFrame(self.master, text="Tabel Pelanggan")
        frame.grid(row=0, columns=1)

        self.pesan = Label(frame, text='', fg='red')
        self.pesan.grid(row=5, column=3)

        ttk.Button(frame, text="Hapus Pelanggan", command=self.hapusplgn).grid(row=8, column=1)
        ttk.Button(frame, text="Update Pelanggan", command=self.updateplgn).grid(row=8, column=2)

        self.tree = ttk.Treeview(frame, height=10, column=("column1", "column2", "column3", "column4"), show='headings')
        self.tree.grid(row=10, column=0, columnspan=5)
        self.tree.heading('#1', text='ID Pelanggan')
        self.tree.column('#1', anchor='center', width=80)
        self.tree.heading('#2', text='Nama Pelanggan')
        self.tree.column('#2', anchor='center', width=100)
        self.tree.heading('#3', text='Alamat')
        self.tree.column('#3', anchor='center', width=80)
        self.tree.heading('#4', text='No Telpon')
        self.tree.column('#4', anchor='center', width=100)

        self.viewing_records()
    # Koneksi database
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
    # Menampilkan data dari tabel data_pelanggan
    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT noplg, nm_plg, alamat, notlp FROM data_pelanggan ORDER BY noplg ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))
    # Hapus data pelanggan
    def hapusplgn(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        for selected_item in self.tree.selection():
            cur.execute("DELETE FROM data_pelanggan WHERE noplg=?", (self.tree.set(selected_item, '#1'),))
            conn.commit()
            self.pesan['text'] = 'Sukses dihapus'
            self.tree.delete(selected_item)
        conn.close()
    # Update data pelanggan
    def updateplgn(self):
        self.pesan['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.pesan['text'] = 'Pilih data yang akan diubah'
            return
        name = self.tree.item(self.tree.selection())['text']
        idplgn = self.tree.item(self.tree.selection())['values'][0]
        nma_plgn = self.tree.item(self.tree.selection())['values'][1]
        alamat = self.tree.item(self.tree.selection())['values'][2]
        notlpn = self.tree.item(self.tree.selection())['values'][3]

        self.updtdbplgn = Toplevel()
        self.updtdbplgn.title = ('Edit Data Pelanggan')
        self.updtdbplgn.resizable(False, False)
        self.updtdbplgn.geometry("400x200")
        frame2 = LabelFrame(self.updtdbplgn, text='Update Data Pelanggan')
        frame2.grid(row=0, column=0, columnspan=3, pady=0)

        self.id_plg = Label(frame2, text='ID Pelanggan: ').grid(row=2, column=0)
        self.id_plgn = Text(frame2, height=1, width=10)
        self.id_plgn.config(font=("consolas", 11), undo=True, wrap='word')
        self.id_plgn.insert(END, idplgn)
        self.id_plgn.grid(row=2, column=2, columnspan=2, sticky=W + E)

        self.nam_plg = Label(frame2, text='Nama Pelanggan: ').grid(row=4, column=0)

        self.nam_plgn = Text(frame2, height=1, width=10)
        self.nam_plgn.config(font=("consolas", 11), undo=True, wrap='word') # Tidak bisa diubah
        self.nam_plgn.insert(END, nma_plgn)
        self.nam_plgn.grid(row=4, column=2, columnspan=2, sticky=W + E)

        self.alamatplg = Label(frame2, text='Alamat: ').grid(row=6, column=0)

        self.alamatplgn = Text(frame2, height=1, width=10)
        self.alamatplgn.config(font=("consolas", 11), undo=True, wrap='word')
        self.alamatplgn.insert(END, alamat)
        self.alamatplgn.grid(row=6, column=2, columnspan=2, sticky=W + E)

        self.no_tlp = Label(frame2, text='No Telepon: ').grid(row=8, column=0)

        self.no_tlpn = Text(frame2, height=1, width=10)
        self.no_tlpn.config(font=("consolas", 11), undo=True, wrap='word')
        self.no_tlpn.insert(END, notlpn)
        self.no_tlpn.grid(row=8, column=2, columnspan=2, sticky=W + E)

        ttk.Button(frame2, text='Update', command=self.simpaneditplgn).grid(row=10, column=2, sticky=W + E)

        self.updtdbplgn.mainloop()

    def simpaneditplgn(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        self.u1 = self.id_plgn.get(1.0, END)
        self.u2 = self.nam_plgn.get(1.0, END)
        self.u3 = self.alamatplgn.get(1.0, END)
        self.u4 = self.no_tlpn.get(1.0, END)
        query = "UPDATE data_pelanggan SET nm_plg=?, alamat=?, notlp=? WHERE noplg=?"
        cur.execute(query, (self.u2, self.u3, self.u4, self.u1))
        conn.commit()
        self.updtdbplgn.destroy()
        self.pesan['text'] = 'Sukses di ubah'
        self.viewing_records()

# Koding Untuk melihat tabel transaksi
class LihatTransaksi:
    db_name = 'dbkom.db'

    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Tabel Transaksi")
        self.master.resizable(False, False)
        frame = LabelFrame(self.master, text="Input Transaksi")
        frame.grid(row=0, columns=1)
        Label(frame, text="ID Faktur: ").grid(row=1, column=0)
        self.idfak = Entry(frame)
        self.idfak.grid(row=1, column=1)
        Label(frame, text="Nama Pelanggan: ").grid(row=2, column=0)
        self.nmplgn = Entry(frame)
        self.nmplgn.grid(row=2, column=1)
        Label(frame, text="Nama Barang: ").grid(row=3, column=0)
        self.nmbrg = Entry(frame)
        self.nmbrg.grid(row=3, column=1)
        Label(frame, text="Jumlah Barang: ").grid(row=4, column=0)
        self.jmlbrg = Entry(frame)
        self.jmlbrg.grid(row=4, column=1)
        Label(frame, text="Total Bayar: ").grid(row=5, column=0)
        self.totalbayar = Entry(frame)
        self.totalbayar.grid(row=5, column=1)

        ttk.Button(frame, text="Tambah Transaksi", command=self.tambahkantrans).grid(row=1, column=2)
        ttk.Button(frame, text="Update Transaksi", command=self.updatetransk).grid(row=6, column=2)
        ttk.Button(frame, text="Hapus Transaksi", command=self.hapustrans).grid(row=6, column=4)

        self.pesan = Label(frame, text='', fg='red')
        self.pesan.grid(row=3, column=3)

        self.tree = ttk.Treeview(frame, height=10, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.tree.grid(row=7, column=0, columnspan=6, padx=5, pady=5)
        self.tree.heading('#1', text='ID Faktur')
        self.tree.column('#1', anchor='center', width=80)
        self.tree.heading('#2', text='Nama Pelanggan')
        self.tree.column('#2', anchor='center', width=100)
        self.tree.heading('#3', text='Nama Barang')
        self.tree.column('#3', anchor='center', width=120)
        self.tree.heading('#4', text='Jumlah Barang')
        self.tree.column('#4', anchor='center', width=100)
        self.tree.heading('#5', text='Total Bayar')
        self.tree.column('#5', anchor='center', width=120)

        self.viewing_records()
    # Koneksi database
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
    # Menampilkan data dari tabel dfaktur
    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT idfak, nm_plgn, nm_brg, jml_brg, totalbyr FROM dfaktur ORDER BY idfak ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))

    def validasi(self):
        return len(self.nmplgn.get()) != 0 and len(self.nmbrg.get()) != 0 and len(self.jmlbrg.get()) != 0 and len(
            self.idfak.get()) != 0 and len(self.totalbayar.get())
    def tambahkantrans(self):
        if self.validasi():
            query = 'INSERT INTO dfaktur VALUES (?, ?, ?, ?, ?)'
            parameters = (self.idfak.get(), self.nmplgn.get(), self.nmbrg.get(), self.jmlbrg.get(), self.totalbayar.get())
            self.run_query(query, parameters)
            self.pesan['text'] = '{} Berhasil Ditambahkan'.format(self.nmbrg.get())
            self.idfak.delete(0, END)
            self.nmplgn.delete(0, END)
            self.nmbrg.delete(0, END)
            self.jmlbrg.delete(0, END)
            self.totalbayar.delete(0, END)

            self.viewing_records()
        else:
            self.viewing_records()
    def hapustrans(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        for selected_item in self.tree.selection():
            cur.execute("DELETE FROM dfaktur WHERE idfak=?", (self.tree.set(selected_item, '#1'),))
            conn.commit()
            self.pesan['text'] = 'Transaksi Telah dihapus'
            self.tree.delete(selected_item)
        conn.close()
    def updatetransk(self):
        self.pesan['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.pesan['text'] = 'Pilih data yang akan diubah'
            return
        name = self.tree.item(self.tree.selection())['text']
        idfakt = self.tree.item(self.tree.selection())['values'][0]
        nma_plgn = self.tree.item(self.tree.selection())['values'][1]
        nma_brg = self.tree.item(self.tree.selection())['values'][2]
        jmlbrg = self.tree.item(self.tree.selection())['values'][3]
        totbyr = self.tree.item(self.tree.selection())['values'][4]

        self.updtdbtransk = Toplevel()
        self.updtdbtransk.title = ('Edit Data Transaksi')
        self.updtdbtransk.resizable(False, False)
        self.updtdbtransk.geometry("240x160")
        frame2 = LabelFrame(self.updtdbtransk, text='Update Data Transaksi')
        frame2.grid(row=0, column=0, columnspan=3, pady=0)

        self.id_fak = Label(frame2, text='ID Faktur: ').grid(row=2, column=0)
        self.id_fakt = Text(frame2, height=1, width=10)
        self.id_fakt.config(font=("consolas", 11), undo=True, wrap='word')
        self.id_fakt.insert(END, idfakt)
        self.id_fakt.grid(row=2, column=2, columnspan=2, sticky=W + E)

        self.nam_plg = Label(frame2, text='Nama Pelanggan: ').grid(row=4, column=0)
        self.nam_plgn = Text(frame2, height=1, width=10)
        self.nam_plgn.config(font=("consolas", 11), undo=True, wrap='word')
        self.nam_plgn.insert(END, nma_plgn)
        self.nam_plgn.grid(row=4, column=2, columnspan=2, sticky=W + E)

        self.nmbrgn = Label(frame2, text='Nama Barang: ').grid(row=6, column=0)
        self.nmabrg = Text(frame2, height=1, width=13)
        self.nmabrg.config(font=("consolas", 11), undo=True, wrap='word')
        self.nmabrg.insert(END, nma_brg)
        self.nmabrg.grid(row=6, column=2, columnspan=2, sticky=W + E)

        self.jml_brg = Label(frame2, text='Jumlah Barang: ').grid(row=8, column=0)
        self.jmlh_brg = Text(frame2, height=1, width=10)
        self.jmlh_brg.config(font=("consolas", 11), undo=True, wrap='word')
        self.jmlh_brg.insert(END, jmlbrg)
        self.jmlh_brg.grid(row=8, column=2, columnspan=2, sticky=W + E)

        self.total_byr = Label(frame2, text='Total Bayar: ').grid(row=10, column=0)
        self.tot_byr = Text(frame2, height=1, width=10)
        self.tot_byr.config(font=("consolas", 11), undo=True, wrap='word')
        self.tot_byr.insert(END, totbyr)
        self.tot_byr.grid(row=10, column=2, columnspan=2, sticky=W + E)

        ttk.Button(frame2, text='Update', command=self.simpanedittrans).grid(row=11, column=2, sticky=W + E)

        self.updtdbtransk.mainloop()
    def simpanedittrans(self):
        conn = sqlite3.connect("dbkom.db")
        cur = conn.cursor()
        self.u1 = self.id_fakt.get(1.0, END)
        self.u2 = self.nam_plgn.get(1.0, END)
        self.u3 = self.nmabrg.get(1.0, END)
        self.u4 = self.jmlh_brg.get(1.0, END)
        self.u5 = self.tot_byr.get(1.0, END)
        query = "UPDATE dfaktur SET nm_plgn=?, nm_brg=?, jml_brg=?, totalbyr=? WHERE idfak=?"
        cur.execute(query, (self.u2, self.u3, self.u4, self.u5, self.u1))
        conn.commit()
        self.updtdbtransk.destroy()
        self.pesan['text'] = 'Sukses diubah'
        self.viewing_records()

class Application1:

    conn = sqlite3.connect("dbkom.db")
    c = conn.cursor()

    # session
    produk_id = []
    nma_brg = []
    hrga_brg = []
    jumlh_brg = []
    jumlh_byr = []

    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Aplikasi Penjualan Komputer")
        self.master.resizable(False, False)
        self.master.iconbitmap('logokom.ico')
        root.withdraw()
        # membuat frame utama aplikasi
        self.left = Frame(master, width=500, height=800, bg='white')
        self.left.grid(column=0, row=5)

        self.right = Frame(master, width=800, height=800, borderwidth = 9, bg='lightblue')
        self.right.grid(column=10, row=5)

        self.heading = Label(self.left, text="Aplikasi Penjualan Komputer", font=('Helvetica 14 bold'), bd=0, bg='white')
        self.heading.place(x=120, y=20)

        # Tabel Invoice
        self.heading = Label(self.right, text="Invoice", font=('calibri 14 bold'), bd=0, fg='white', bg='lightblue')
        self.heading.place(x=300, y=0)

        self.nmbrg = Label(self.right, text="Nama Barang", font=('calibri 14 bold'), fg='white', bg='lightblue')
        self.nmbrg.place(x=0, y=25)

        self.jmlhbrg = Label(self.right, text="Jumlah",font=('calibri 14 bold'), fg='white', bg='lightblue')
        self.jmlhbrg.place(x=550, y=25)

        self.jmlhbrg = Label(self.right, text="Harga Barang", font=('calibri 14 bold'), fg='white', bg='lightblue')
        self.jmlhbrg.place(x=250, y=25)

        # Entri Data
        self.kdobrg = Label(self.left, text="Kode Barang", font=('calibri 15 bold'), fg='yellowgreen', bg='white')
        self.kdobrg.place(x=0, y=90)
        self.kdobrg_ent = Entry(self.left, width=25, bg='lightblue')
        self.kdobrg_ent.place(x=145, y=95)
        self.kdobrg_ent.focus()
        self.submit = Button(self.left, text="Search", width=20, height=2, bd=0, bg='dimgrey', activebackground='lightgray',
                             activeforeground='black', fg='lightgray', command =self.ajax)
        self.submit.place(x=225, y=125)

        self.nmbrg = Label(self.left, text="", font=('calibri 18 bold'), fg='yellowgreen', bg='white')
        self.nmbrg.place(x=0, y=190)
        self.hrgbrg = Label(self.left, text="", font=('calibri 18 bold'), fg='yellowgreen', bg='white')
        self.hrgbrg.place(x=0, y=220)
        self.stok = Label(self.left, text="", font=('calibri 18 bold'), fg='yellowgreen', bg='white')
        self.stok.place(x=0, y=250)

        self.totalbyr = Label(self.right, text="", font=('calibri 18 bold'), fg='white', bg='lightblue')
        self.totalbyr.place(x=0, y=600)
        self.lihatbarang = Button(self.left, text="Lihat Barang", width=20, height=4, bd=0, bg='greenyellow',
                                  activebackground='lightgray',
                                  activeforeground='black', fg='black', command=self.lihatbrg)
        self.lihatbarang.place(x=0, y=540)
        self.lihattransaksi = Button(self.left, text="Lihat Transaksi", width=20, height=4, bd=0, bg='greenyellow',
                                     activebackground='lightgray',
                                     activeforeground='black', fg='black', command=self.lihatrans)
        self.lihattransaksi.place(x=150, y=540)
        self.lihatplg = Button(self.left, text="Lihat Pelanggan", width=20, height=4, bd=0, bg='greenyellow',
                               activebackground='lightgray',
                               activeforeground='black', fg='black', command=self.lihatplgn)
        self.lihatplg.place(x=300, y=540)
        self.quit = Button(self.left, text="Keluar", width=20, height=4, bd=0, bg='tomato',
                               activebackground='lightgray',
                               activeforeground='black', fg='black', command= self.close_window)
        self.quit.place(x=300, y=615)

    def close_window(self):
        root.destroy()

    def ajax(self, *args, **kwargs):
        conn = sqlite3.connect("dbkom.db")
        c = conn.cursor()
        self.kode_brg = self.kdobrg_ent.get()
        query = "SELECT * FROM data_brg where kode_brg=?"
        result = c.execute(query, (self.kode_brg))
        for self.r in result:
            self.get_kode_brg = self.r[0]
            self.get_nm_brg = self.r[1]
            self.get_hrg_brg = self.r[2]
            self.get_stok = self.r[3]
        self.nmbrg.configure(text="Nama Barang  :  " + str(self.get_nm_brg))
        self.hrgbrg.configure(text="Harga Barang : Rp. " + str(self.get_hrg_brg))
        self.stok.configure(text="Stok Barang :   " + str(self.get_stok))

        # Input Data Pembeli
        self.namaplg = Label(self.left, text="Nama Pembeli", font=('calibri 15 bold'), fg='yellowgreen', bg='white')
        self.namaplg.place(x=0, y=365)
        self.namaplg_ent = Entry(self.left, width=25, bg='lightblue')
        self.namaplg_ent.place(x=190, y=370)
        self.namaplg_ent.focus()
        self.notlpn = Label(self.left, text="No Telepon", font=('calibri 15 bold'), fg='yellowgreen', bg='white')
        self.notlpn.place(x=0, y=400)
        self.notlpn_ent = Entry(self.left, width=25, bg='lightblue')
        self.notlpn_ent.place(x=190, y=405)
        self.alamatplg = Label(self.left, text="Alamat", font=('calibri 15 bold'), fg='yellowgreen', bg='white')
        self.alamatplg.place(x=0, y=440)
        self.alamatplg_ent = Entry(self.left, width=25, bg='lightblue')
        self.alamatplg_ent.place(x=190, y=445)
        self.alamatplg_ent.focus()
        self.jmlhbrg = Label(self.left, text="Jumlah Barang", font=('calibri 15 bold'), fg='yellowgreen', bg='white')
        self.jmlhbrg.place(x=0, y=280)
        self.jmlhbrg_ent = Entry(self.left, width=25, bg='lightblue')
        self.jmlhbrg_ent.place(x=190, y=290)
        self.tambahkan = Button(self.left, text="Tambahkan", width=20, height=2, bd=0, bg='dimgrey',
                                activebackground='lightgray',
                                activeforeground='black', fg='lightgray', command=self.tmbhkan)
        self.tambahkan.place(x=230, y=470)
        self.cetakfkt = Button(self.left, text="Cetak Ke Invoice", width=20, height=2, bd=0, bg='dimgrey',
                               activebackground='lightgray',
                               activeforeground='black', fg='lightgray', command=self.cetakinvo)
        self.cetakfkt.place(x=230, y=320)

    def tmbhkan(self, *args, **kwargs):
        conn = sqlite3.connect("dbkom.db")
        c = conn.cursor()

        self.nm_brg = str(self.get_nm_brg)
        self.jml_brg = int(self.jmlhbrg_ent.get())
        self.nm_plg = self.namaplg_ent.get()
        self.alamat = self.alamatplg_ent.get()
        self.notlp = self.notlpn_ent.get()
        self.nm_brg = str(self.get_nm_brg)
        self.jml_byr = str(jumlh_byr)
        if self.nm_plg == '' or self.notlp == '' or self.alamat == '':
            tkinter.messagebox.showinfo("Warning", "Isi semua kolom")
        else:
            # Input Data Pelanggan ke Database
            sql3 = "INSERT INTO dfaktur (nm_plgn, nm_brg, jml_brg, totalbyr) VALUES(?, ?, ?, ?)"
            c.execute(sql3, (self.nm_plg, self.nm_brg, self.jml_brg, self.jml_byr))
            conn.commit()
            sql2 = "INSERT INTO data_pelanggan (nm_plg, notlp, alamat) VALUES(?, ?, ?)"
            c.execute(sql2, (self.nm_plg, self.notlp, self.alamat))
            conn.commit()
            sql = "INSERT INTO faktur (nm_plg, notlp, alamat, jml_brg, nm_brg) VALUES(?, ?, ?, ?, ?)"
            c.execute(sql, (self.nm_plg, self.notlp, self.alamat, self.jml_brg, self.nm_brg))
            conn.commit()
            tkinter.messagebox.showinfo("Sukses", "Data Berhasil disimpan")

    def lihatbrg(self):
        root2 = Toplevel(self.master)
        brglht = LihatBarang(root2)

    def lihatplgn(self):
        root3 = Toplevel(self.master)
        plgnlht = LihatPelanggan(root3)

    def lihatrans(self):
        root4 = Toplevel(self.master)
        plgnlht = LihatTransaksi(root4)

    def cetakinvo(self, *args, **kwargs):
            self.nm_brg = str(self.get_nm_brg)
            self.hrg_brg = str(self.get_hrg_brg)
            self.jml_brg = int(self.jmlhbrg_ent.get())
            if self.jml_brg > int(self.get_stok):
                tkinter.messagebox.showinfo("Error", "Maaf, Stok Barang Kurang")
            else:
                self.jml_byr = float(self.jml_brg) * (self.get_hrg_brg)
                nma_brg.append(self.get_nm_brg)
                hrga_brg.append(self.get_hrg_brg)
                jumlh_byr.append(self.jml_byr)
                jumlh_brg.append(self.jml_brg)
                produk_id.append(self.get_kode_brg)

                self.y_index = 50
                self.x_index = 0
                self.counter = 0

                for self.p in nma_brg:
                    self.tempnmbrg = Label(self.right, text=str(nma_brg[self.counter]), font=('calibri 12 bold'),
                                           fg='white', bg='lightblue')
                    self.tempnmbrg.place(x=0, y=self.y_index)
                    self.temphrgbrg = Label(self.right, text=str(hrga_brg[self.counter]), font=('calibri 12 bold'),
                                            fg='white', bg='lightblue')
                    self.temphrgbrg.place(x=250, y=self.y_index)
                    self.tempjmlhbrg = Label(self.right, text=str(jumlh_brg[self.counter]), font=('calibri 12 bold'),
                                             fg='white', bg='lightblue')
                    self.tempjmlhbrg.place(x=550, y=self.y_index)
                    self.tempjmlhbyr = Label(self.right, text=str(jumlh_byr[self.counter]), font=('calibri 14 bold'),
                                             fg='white', bg='lightblue')
                    self.y_index += 30
                    self.counter += 1
                    # Jumlah Bayar
                    self.totalbyr.configure(text="Total Bayar: " + str(sum(jumlh_byr)))
                    # Clear Data
                    self.jmlhbrg.place_forget()
                    self.jmlhbrg_ent.place_forget()
                    self.cetakfkt.destroy()
                    self.nmbrg.configure(text="")
                    self.hrgbrg.configure(text="")
                    self.stok.configure(text="")
                    # Fokus ke search dan kode barang
                    self.kdobrg.focus()
                    self.kdobrg_ent.delete(0, END)


root = Tk()
app = Utama(root)
root.iconbitmap('logokom.ico')
root.title('Aplikasi Penjualan Komputer')
root.mainloop()