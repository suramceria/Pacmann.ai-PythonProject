# -*- coding: utf-8 -*-
"""Pacmann Python I-II Project: Super Cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aJchh5-ta1kAl0Wx3QsR-o-vXwmkBIKm
"""

#%%writefile -a super_cashier.py
import pandas as pd
import numpy as np
import sys


class Transaction(object):
    
    def __init__(self, id):
          """Memulai transaksi dengan memasukkan id transaksi, dengan susunan: id_transaksi = Transaction("nama_pengguna"). Contoh: user_yudis = Transaction("Yudis:)"""
          self.id = id
          self.nama_item = nama_item = [] #menampung list nama item tiap id pelanggan
          self.nama_temp = nama_temp = set() #menampung sementara nama-nama item yg diorder untuk disortir dari input duplikat
          self.jumlah_item = jumlah_item = [] #menampung list jumlah tiap item
          self.harga_item = harga_item = [] #menampung list harga tiap item
          self.total_harga = total_harga = [] #menampung penghitungan total harga tiap item (jumlah * harga)
        
    def Penghitungan(self):
            """Method ini digunakan untuk mempersilahkan user untuk mulai memasukkan nama item, 
            jumlah item & harga per item dari awal. Serta memungkinkan user untuk mengubah, menghapus, 
            menambah, juga mengulang pesanan dengan mengisi input yang disediakan. Contoh memulai: user_1.Penghitungan("Yudis")"""
            #memastikan bahwa tiap list dikosongkan sebelum memulai transaksi baru tiap id
            self.nama_item.clear()
            self.nama_temp.clear()
            self.jumlah_item.clear()
            self.harga_item.clear()
            self.total_harga.clear()

            #menyusun dictionary mapping, mengambil data dari tampungan list sebelumnya, yang kemudian diterjemahkan ke dalam tabel pandas DataFrame
            dict_transaksi = {
                "Nama item": self.nama_item,
                "Jumlah item": self.jumlah_item,
                "Harga item": self.harga_item,
                "Total harga": self.total_harga}

            #menyusun tabel DataFrame dengan dict_transaksi sebagai acuannya
            tabel = pd.DataFrame(dict_transaksi)
            tabel.index = np.arange(1, len(tabel) + 1)
            total_belanja = tabel["Total harga"].sum()
            tabel.loc['Total', 'Total harga'] = total_belanja
            tabel_transaksi = tabel.fillna('-')

            while True:
              try:
                  jenis_item = int(input("Berapa jenis item yang ingin Anda beli?: ")) #user menentukan banyaknya jenis item yang ingin dibeli
                  break
              except ValueError:
                  print("Input harus berupa angka. Silahkan coba lagi.")
              
            #user melakukan input nama, jumlah & harga item sebanyak baris sebanyak jumlah jenis item yang dikehendaki oleh user
            for i in range (1, jenis_item+1):
                while True:
                  nama = input(f"\nNama item ke-{i}     : ")
                  if not nama.strip():
                    print("Input nama item tidak boleh kosong!")
                    continue
                  if nama in self.nama_temp: #memerintahkan untuk menghapus nilai input yang sudah dimasukkan sebelumnya, dan mengulangi proses input
                    print("Nama item sudah ada, jika ingin menambah jumlah item tsb, bisa diatur di sesi berikutnya.")
                    continue
                  break
                self.nama_temp.add(nama)
                self.nama = nama
                while True:                    
                  try:
                    self.jumlah = int(input(f"Jumlah item ke-{i}   : "))
                    break
                  except ValueError:
                    print("Input jumlah item harus berupa angka!")
                while True:
                  try:
                    self.harga = int(input(f"Harga per item ke-{i}: "))
                    break
                  except ValueError:
                    print("Input harga per item harus berupa angka!")
                self.hitung = self.harga * self.jumlah
                i += 1     
                self.nama_item.append(self.nama)
                self.jumlah_item.append(self.jumlah)
                self.harga_item.append(self.harga)
                self.total_harga.append(self.hitung)
            dict_transaksi = {
                "Nama item": self.nama_item,
                "Jumlah item": self.jumlah_item,
                "Harga item": self.harga_item,
                "Total harga": self.total_harga}
            tabel = pd.DataFrame(dict_transaksi)
            tabel.index = np.arange(1, len(tabel) + 1)
            total_belanja = tabel["Total harga"].sum()
            tabel.loc['Total', 'Total harga'] = total_belanja
            tabel_transaksi = tabel.fillna('-')
            
            
            print("\n")
            print(tabel_transaksi)
        
            print("\n==================Daftar perintah==================")
            print("Ketik 'ubah' untuk memperbarui pesanan")
            print("Ketik 'tambah' untuk menambah baris daftar pesanan")
            print("Ketik 'hapus' untuk menghapus baris daftar pesanan")
            print("Ketik 'lanjut' untuk meneruskan proses transaksi")
            print("Ketik 'batal' untuk membatalkan transaksi")
            print("Ketik 'reset' untuk mengulang transaksi")
    
            while True:
                    try :
                        pilihan = str(input("\nTindakan apa yang ingin dilakukan?(ubah/tambah/hapus/lanjut/batal/reset): "))
                        pilihan = pilihan.lower()
                        if pilihan == "ubah":
                          self.index = int(input("Masukan urutan index item yang ingin diubah: "))
                          self.index = self.index - 1    
                          print(f"Masukan kolom(nama, jumlah atau harga) apa yang ingin diubah (index-{self.index+1}): ")
                          self.kolom = str(input())
                          kolom = self.kolom
                          kolom = kolom.lower()

                          if kolom == "nama":
                                  self.nama = input(f"Masukkan nama item index ke-{self.index+1} yang baru: ")
                                  if self.nama.strip() == "":
                                    raise ValueError("Input tidak boleh kosong")
                                  self.nama_item[self.index] = self.nama 
                                  dict_transaksi #memanggil kembali dictionary, agar memperbarui value sesuai input yang baru saja dilakukan.
                                  tabel = pd.DataFrame(dict_transaksi)
                                  tabel.index = np.arange(1, len(tabel) + 1)
                                  total_belanja = tabel["Total harga"].sum()
                                  tabel.loc['Total', 'Total harga'] = total_belanja
                                  tabel_transaksi = tabel.fillna('-')
                                  print("\n")
                                  print(tabel_transaksi)

                          elif kolom == "jumlah": 
                                  self.jumlah = int(input(f"Masukkan jumlah item index ke-{self.index+1} yang baru: "))
                                  self.jumlah_item[self.index] = self.jumlah
                                  self.total_harga[self.index] = self.harga_item[self.index] * self.jumlah_item[self.index]
                                  dict_transaksi                               
                                  tabel = pd.DataFrame(dict_transaksi)
                                  tabel.index = np.arange(1, len(tabel) + 1)
                                  total_belanja = tabel["Total harga"].sum()
                                  tabel.loc['Total', 'Total harga'] = total_belanja
                                  tabel_transaksi = tabel.fillna('-')
                                  print("\n")
                                  print(tabel_transaksi)

                          elif kolom == "harga":
                                  self.harga = int(input(f"Masukkan harga item index ke-{self.index+1} yang baru: "))
                                  self.harga_item[self.index] = self.harga
                                  self.total_harga[self.index] = self.harga_item[self.index] * self.jumlah_item[self.index]
                                  dict_transaksi                                
                                  tabel = pd.DataFrame(dict_transaksi)
                                  tabel.index = np.arange(1, len(tabel) + 1)
                                  total_belanja = tabel["Total harga"].sum()
                                  tabel.loc['Total', 'Total harga'] = total_belanja
                                  tabel_transaksi = tabel.fillna('-')
                                  print("\n")
                                  print(tabel_transaksi)

                          else:
                              print("Input tidak sesuai!")
                              continue;

                          continue;
                        
                        elif pilihan == "tambah":
                            try:
                                banyak_baris = int(input("\nMasukan banyak baris baru yang akan dibuat: "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                banyak_baris = int(input("\nMasukan banyak baris baru yang akan dibuat: "))
                            for i in range(1, banyak_baris+1):
                              while True:
                                self.nama = str(input(f"\nNama item baru ke-{i}     : "))
                                self.nama_item.append(self.nama)
                                if not self.nama.strip():
                                  print("Input nama item tidak boleh kosong!")
                                  continue
                                if self.nama in self.nama_temp: #memerintahkan untuk menghapus nilai input duplikat, dan mengulangi proses input
                                  print("Nama item sudah ada, jika ingin menambah jumlah item tsb, bisa diatur di sesi berikutnya.")
                                  continue
                                break
                              self.nama_temp.add(self.nama)
                              self.nama = nama
                   
                              while True:
                                try:
                                  self.jumlah = int(input(f"Jumlah item baru ke-{i}   : ")) 
                                  self.jumlah_item.append(self.jumlah)
                                  break
                                except ValueError:
                                  print("Input jumlah item harus berupa angka!")
                              
                              while True:
                                try:
                                  self.harga = int(input(f"Harga per item baru ke-{i}: "))
                                  self.harga_item.append(self.harga)
                                  break
                                except ValueError:
                                  print("Input harga per item harus berupa angka!")
                                                   
                              i += 1

                              self.hitung = self.jumlah * self.jumlah
                              self.total_harga.append(self.hitung)
                            dict_transaksi = {
                                "Nama item": self.nama_item,
                                "Jumlah item": self.jumlah_item,
                                "Harga item": self.harga_item,
                                "Total harga": self.total_harga}
                            tabel = pd.DataFrame(dict_transaksi)
                            tabel.index = np.arange(1, len(tabel) + 1)
                            total_belanja = tabel["Total harga"].sum()
                            tabel.loc['Total', 'Total harga'] = total_belanja
                            tabel_transaksi = tabel.fillna('-')                             
                            print("\n")
                            print(tabel_transaksi)

                            continue;

                        elif pilihan == "hapus":
                          banyak_baris = int(input("Berapa banyak baris yang ingin dihapus?: "))
                          for i in range(banyak_baris):
                            self.index = int(input("Urutan index yang ingin dihapus: "))
                            self.index = self.index - 1  #input index dikurangi dg 1, utk menyesuaikan index yg sudah di-adjust mjd dimulai dari 1                
                            self.nama_item.pop(self.index) 
                            self.jumlah_item.pop(self.index)
                            self.harga_item.pop(self.index)
                            self.total_harga.pop(self.index)
                            dict_transaksi
                            tabel = pd.DataFrame(dict_transaksi)
                            tabel.index = np.arange(1, len(tabel) + 1)
                            total_belanja = tabel["Total harga"].sum()
                            tabel.loc['Total', 'Total harga'] = total_belanja
                            tabel_transaksi = tabel.fillna('-')                       
                            print("\n")
                            print(tabel_transaksi)

                          continue;

                        elif pilihan == "reset": #membersihkan semua isi dari daftar
                          self.nama_item.clear()
                          self.nama_temp.clear()
                          self.jumlah_item.clear()
                          self.harga_item.clear()
                          self.total_harga.clear()
                          print("Semua pesanan sudah dikosongkan")

                          pilihan = str(input("\nTindakan apa yang ingin dilakukan?(tambah/batal): "))
                          pilihan = pilihan.lower()

                          if pilihan == "tambah":
                            try:
                                banyak_baris = int(input("\nMasukan banyak baris baru yang akan dibuat: "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                banyak_baris = int(input("\nMasukan banyak baris baru yang akan dibuat: "))
                            for i in range(1, banyak_baris+1):
                              while True:
                                self.nama = str(input(f"\nNama item baru ke-{i}     : "))
                                self.nama_item.append(self.nama)
                                if not self.nama.strip():
                                  print("Input nama item tidak boleh kosong!")
                                  continue
                                if self.nama in self.nama_temp: #memerintahkan untuk menghapus nilai input duplikat, dan mengulangi proses input
                                  print("Nama item sudah ada, jika ingin menambah jumlah item tsb, bisa diatur di sesi berikutnya.")
                                  continue
                                break
                              self.nama_temp.add(self.nama)
                              self.nama = nama
                   
                              while True:
                                try:
                                  self.jumlah = int(input(f"Jumlah item baru ke-{i}   : ")) 
                                  self.jumlah_item.append(self.jumlah)
                                  break
                                except ValueError:
                                  print("Input jumlah item harus berupa angka!")
                              
                              while True:
                                try:
                                  self.harga = int(input(f"Harga per item baru ke-{i}: "))
                                  self.harga_item.append(self.harga)
                                  break
                                except ValueError:
                                  print("Input harga per item harus berupa angka!")
                                                   
                              i += 1

                              self.hitung = self.jumlah * self.jumlah
                              self.total_harga.append(self.hitung)
                            dict_transaksi = {
                                "Nama item": self.nama_item,
                                "Jumlah item": self.jumlah_item,
                                "Harga item": self.harga_item,
                                "Total harga": self.total_harga}
                            tabel = pd.DataFrame(dict_transaksi)
                            tabel.index = np.arange(1, len(tabel) + 1)
                            total_belanja = tabel["Total harga"].sum()
                            tabel.loc['Total', 'Total harga'] = total_belanja
                            tabel_transaksi = tabel.fillna('-')                             
                            print("\n")
                            print(tabel_transaksi)

                            continue;

                          elif pilihan == "batal":
                            sys.exit("Proses transaksi dibatalkan")

                          else:
                            print("Input tidak sesuai!")

                          continue;

                        elif pilihan == "lanjut" :
                            print("Lanjut ke proses berikutnya")
                            break;
                        
                        elif pilihan == "batal":
                            sys.exit("Proses transaksi dibatalkan")
                                        
                        else :
                            print("Inputan Kode salah, Lihat kode di daftar perintah !")
                        
                    except ValueError:
                        continue
            
            def Diskon(self):
              """Method ini bertugas untuk menghitung diskon berdasarkan total keseluruhan belanja
              dari item paling awal hingga akhir yang akan dimasukkan ke dalam variabel total_belanja. 
              Jika total_belanja > 200.000 maka diskon 5%, >300.000 maka diskon 8% & >500.000 maka
              diskon 10%. Perhitungannya yaitu = [total_belanja - (total_belanja*diskon%)]."""
            while True:
              try:
                self.name = str(input("\nPesanan atas nama: "))
                nama = self.name
                dict_transaksi = {
                  "Nama item": self.nama_item,
                  "Jumlah item": self.jumlah_item,
                  "Harga item": self.harga_item,
                  "Total harga": self.total_harga}
                tabel = pd.DataFrame(dict_transaksi)
                tabel.index = np.arange(1, len(tabel) + 1)
                total_belanja = tabel["Total harga"].sum()
                tabel.loc['Total', 'Total harga'] = total_belanja
                tabel_transaksi = tabel.fillna('-')
      
                if self.name == nama:
                  if total_belanja <= 200_000:
                    print("Maaf, nominal belanja Anda belum memenuhi kriteria mendapatkan diskon. (min. Rp. 200,001)")
                    print(f"Harga yang harus Anda bayar sebesar: Rp. {total_belanja:,}")
                    break;

                  elif total_belanja > 200_000 and total_belanja <= 300_000:
                    nominal_diskon = total_belanja * 0.05
                    total_akhir = total_belanja - nominal_diskon
                    print(f"Selamat! Pembeli a/n {self.name} mendapat diskon sebesar 5%")
                    print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
                    print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
                    print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")
                    break;

                  elif total_belanja > 300_000 and total_belanja <= 500_000:
                    nominal_diskon = total_belanja * 0.08
                    total_akhir = total_belanja - nominal_diskon
                    print(f"Selamat! Pembeli a/n {self.name} mendapat diskon sebesar 8%")
                    print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
                    print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
                    print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")
                    break;

                  else:
                    nominal_diskon = total_belanja *0.1
                    total_akhir = total_belanja - nominal_diskon
                    print(f"Selamat! Pembelian a.n {self.name} mendapat diskon sebesar 10%")
                    print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
                    print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
                    print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")
                    
                    break;

                else:
                  print("Input atas nama tidak boleh kosong!")

              except ValueError:
                      continue;

            print("\n\nJika ingin melakukan perintah tambahan setelah ini, Anda dapat memanggil metode:")
            print("add_item(nama, jumlah, harga)")
            print("update_item_name('nama', 'update_nama')")
            print("update_item_qty('nama', update_jumlah)")
            print("update_item_price('nama', update_harga)")
            print("delete_item('nama')")
            print("check_order()")
            print("reset_transaction()")
            print("total_price()")
            print("\nJika ada pesan atau fitur tambahan yang ingin ditambahkan oleh rekan-rekan sekalian,")
            print("saya akan dengan senang hati menerimanya baik berupa saran maupun coding-nya.")
            print("\nBila perlu penjelasan mengenai metode di atas, dapat gunakan metode: help(Transaction)")

    def add_item(self, nama, jumlah, harga):
          """Method ini bertugas untuk mempersilahkan user menambah item beserta jumlah dan harganya
          ke dalam daftar belanjaannya. Contoh: add_item("Bakso", 3, 11000)"""
          if nama in self.nama_item:
            print(f"Item {nama} sudah ada dalam daftar pesanan. Mohon masukkan nama item yang berbeda.")
          else:
            self.nama_item.append(nama)
            self.jumlah_item.append(jumlah)
            self.harga_item.append(harga)
            self.hitung=harga*jumlah
            self.total_harga.append(self.hitung)
          dict_transaksi = {
              "Nama item": self.nama_item,
              "Jumlah item": self.jumlah_item ,
              "Harga item": self.harga_item,
              "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')
          print(tabel_transaksi)
          print(f"Item {nama} telah ditambahkan ke dalam daftar pesanan.")

    def update_item_name(self, nama_item_x, update_nama):
          """Method ini untuk memperbarui nama item yang sebelumnya sudah diinput oleh user dengan memasukkan nama 
          item yang ingin diubah, dan nama item baru penggantinya. Contoh: update_item_name("Es teh", "Es jeruk")."""
          if update_nama in self.nama_item:
            print(f"Item {update_nama} sudah ada dalam daftar pesanan. Mohon masukkan nama item yang berbeda.")
          else:
            found = False
            for i in range(len(self.nama_item)):
              if self.nama_item[i] == nama_item_x:
                self.nama_item[i] = update_nama
                found = True
                break;
            if not found:
              print("Nama tidak ditemukan. Coba gunakan method check_order()")
              return
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')
          print(tabel_transaksi)
          print(f"Nama item {nama_item_x} telah diubah menjadi {update_nama}.")

    def update_item_qty(self, nama_item_x, update_jumlah):
          """Method ini untuk memperbarui jumlah dari suatu item yang sebelumnya sudah diinput oleh user dengan 
          memasukkan nama item yang jumlahnya ingin diubah, dan jumlah baru penggantinya. Contoh: 
          update_item_qty("Es teh", 2)."""
          found = False
          for i in range(len(self.jumlah_item)):
            if self.nama_item[i] == nama_item_x:
              self.jumlah_item[i] = update_jumlah
              self.total_harga[i] = self.jumlah_item[i] * self.harga_item[i]
              found = True
              break;
          if not found:
            print("Nama item tidak ditemukan. Coba gunakan method check_order()")
            return 
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')
          print(tabel_transaksi)
          print(f"Jumlah item {nama_item_x} telah diubah menjadi sebanyak {update_jumlah}.")

    def update_item_price(self, nama_item_x, update_harga):
          """Method ini untuk memperbarui harga per item dari suatu item yang sebelumnya sudah diinput oleh user 
          dengan memasukkan nama item yang harganya ingin diubah, dan harga baru penggantinya. 
          Contoh: update_item_price("Es teh", 2)."""
          found = False
          for i in range(len(self.jumlah_item)):
            if self.nama_item[i] == nama_item_x:
              self.harga_item[i] = update_harga
              self.total_harga[i] = self.jumlah_item[i] * self.harga_item[i]
              found = True
              break;
          if not found:
            print("Nama item tidak ditemukan. Coba gunakan method check_order()")
            return  
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')
          print(tabel_transaksi)
          print(f"Harga item {nama_item_x} telah diubah menjadi sebesar Rp. {update_harga:,}.")

    def delete_item(self, nama_item_x):
          """Method ini berguna untuk menghapus item yang dipesan dari daftar pesanan. Contoh: delete_item("Es jeruk")"""
          found = False
          for i in range(len(self.nama_item)):
            if self.nama_item[i] == nama_item_x:
              self.nama_item.pop(i)
              self.jumlah_item.pop(i)
              self.harga_item.pop(i)
              self.total_harga.pop(i)
              found = True
              break
          if not found:
            print("Nama item tidak ditemukan. Coba gunakan method check_order()")
            return
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel=pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')  
          print(tabel_transaksi)
          print(f"Item {nama_item_x} telah dihapus dari daftar pesanan.")
                        
    def check_order(self, id):
          """Method yang bertugas untuk menampilkan daftar pesanan terakhir yang dimuat & mempersilakan pengguna 
          untuk melakukan pengecekan kembali terhadap pesanannya."""
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          tabel.index = np.arange(1, len(tabel) + 1)
          total_belanja = tabel["Total harga"].sum()
          tabel.loc['Total', 'Total harga'] = total_belanja
          tabel_transaksi = tabel.fillna('-')
          print(tabel_transaksi)

          minus_found = False
          for i in self.jumlah_item:
            if i < 0:
              minus_found = True
              print("Warning: Jumlah item tidak boleh minus!")
              break

          for i in self.harga_item:
            if i < 0:
              minus_found = True
              print("Warning: Harga item tidak boleh minus!")
              break

          if not minus_found:
            print("Jumlah & harga item sudah sesuai.")

    def reset_transaction(self, id):
          """Method yang berguna untuk menghapus semua daftar pesanan yang sudah diisi sebelumnya, agar pengguna 
          dapat mengisi ulang dari awal tanpa menghapus satu per satu."""
          self.nama_item.clear()
          self.nama_temp.clear()
          self.jumlah_item.clear()
          self.harga_item.clear()
          self.total_harga.clear()
          
          print("\nSemua pesanan sudah dikosongkan.")

    def total_price(self, id):
          """Method yang berguna untuk memunculkan jumlah harga belanja pengguna, dengan disertai penghitungan diskon berdasarkan kriteria jumlah belanjaannya
          di mana <=200,000 maka tidak mendapat diskon; >200,000 s/d <=300,000 akan mendapat diskon 5%; >300,000 <=500,000 diskon 8% & >500,000 diskon 10%"""
          dict_transaksi = {
            "Nama item": self.nama_item,
            "Jumlah item": self.jumlah_item,
            "Harga item": self.harga_item,
            "Total harga": self.total_harga}
          tabel = pd.DataFrame(dict_transaksi)
          total_belanja = tabel["Total harga"].sum()
          nama = str(input("\nPesanan atas nama: "))
                  
          if total_belanja <= 200_000:
            print("Maaf, nominal belanja Anda belum memenuhi kriteria mendapatkan diskon. (min. Rp. 200,100)")
            print(f"Harga yang harus Anda bayar sebesar:2 Rp. {total_belanja:,}.")

          elif total_belanja > 200_000 and total_belanja <= 300_000:
            nominal_diskon = total_belanja * 0.05
            total_akhir = total_belanja - nominal_diskon
            print(f"Selamat! Pembeli a/n {nama} mendapat diskon sebesar 5%")
            print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
            print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
            print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")

          elif total_belanja > 300_000 and total_belanja <= 500_000:
            nominal_diskon = total_belanja * 0.08
            total_akhir = total_belanja - nominal_diskon
            print(f"Selamat! Pembeli a/n {nama} mendapat diskon sebesar 8%")
            print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
            print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
            print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")

          else:
            nominal_diskon = total_belanja * 0.1
            total_akhir = total_belanja - nominal_diskon
            print(f"Selamat! Pembeli a/n {nama} mendapat diskon sebesar 10%")
            print(f"Jumlah harga belanja sebelum diskon sebesar: Rp. {total_belanja:,}")
            print(f"Besar nominal diskon yang didapat sebesar  : Rp. {nominal_diskon:,}")
            print(f"Harga setelah diskon menjadi sebesar       : Rp. {total_akhir:,}")