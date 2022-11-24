# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:21:56 2022

@author: putri
"""

def make_file():
    file = open('praktikum_ke_9.txt',"w")
    nama = str(input("masukan nama anda :"))
    nim = str(input("masukan nim anda :"))
    angkatan = str(input("masukan tahun angkatan anda:"))
    file.write("Nama :"+ nama)
    file.write("\nNim :" + nim)
    file.write("\nAngkatan :"+ angkatan)
    file.close()
    
def read_file():
    file = open("praktikum_ke_9.txt","r")
    text = file.read()
    print(text)
    file.close()

def add_file():
    file = open("praktikum_ke_9.txt","a")
    sahabat = str(input("masukan nama sahabatmu :"))
    catatan = str(input("masukan catatanmu :"))
    file.write("Sahabatmu :"+ sahabat)
    file.write("catatanmu :" + catatan)
    file.close()
    
def panggil_file():
    ulang = True
    while(ulang):
        print("===Program File Handlling===")
        print("1.Membuat dan Membaca file")
        print("2.Membaca file")
        print("3.Menambahkan text dalam file")
        print("4.Keluar dari program")
        pilih = int(input("masukan angka yang ingin kalian pilih :"))
        
        if(pilih == 1):
            print("\n")
            make_file()
            print("\n")
            
        elif(pilih == 2):
            print("\n")
            read_file()
            print("\n")
            
        elif(pilih == 3):
            print("\n")
            add_file()
            print("\n")
            
        elif(pilih == 4):
            print("terimakasih sudah menggunakan program ini !")
            ulang = False
            
panggil_file()
        
        
        
        
        
    
    
    
    
    
    