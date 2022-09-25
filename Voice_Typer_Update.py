import time
import pyrebase
from zipfile import ZipFile
#import struct
import shutil
import os
import socket
def checking():
    try:
        #socket.create_connection(('Google.com', 80))
        socket.create_connection(("1.1.1.1", 53))
        return True
    except Exception:
        return False


firebaseConfig = {
    "apiKey": "AIzaSyCohmb-xbwVMH7LN3gL2BhSNM1Uy4ZojNA",
    "authDomain": "voice-typer-beta.firebaseapp.com",
    "projectId": "voice-typer-beta",
    "storageBucket": "voice-typer-beta.appspot.com",
    "messagingSenderId": "459931259449",
    "appId": "1:459931259449:web:0b263ed7254f748d1273e8",
    "measurementId": "G-46YPRNMMKZ",
    "databaseURL": "https://voice-typer-beta-default-rtdb.firebaseio.com"
}

Firebase = pyrebase.initialize_app(firebaseConfig)
storage = Firebase.storage()
database = Firebase.database()
file = open(r"C:\ProgramData\App_version.txt", 'r')
current_version = file.read()
file.close()
to_check = checking()
if to_check == True:
    Server_Version = database.get()
    Server_version = str(Server_Version.val()).replace("OrderedDict", "").replace("(", "").replace(")" ,"").replace("[" ,"").replace("]" ,"").replace("'" ,"").replace("Beta" ,"").replace("," ,"").replace("Nope" ,"").replace(" " ,"").replace("Version","")
    print(Server_version)
    try:
        if current_version != Server_version:
            print("Voice Typer new version available, installing update DO NOT CLOSE THIS")
            Path_on_cloud = "VoiceTyper/Voice_Typer_Setup.zip"
            storage.child(Path_on_cloud).download("Voice_Typer.zip")
            file = "Voice_Typer.zip"
            print("download of voice typer completed")
            time.sleep(5)
            with ZipFile(file,'r') as zip:
                zip.printdir()
                print("extracting...")
                zip.extractall()
                print("Extracted")
                #os.popen("Delete.cmd")
                filen = open(r"C:\ProgramData\App_version.txt", 'r')
                filen.write(Server_version)
                filen.close()
                root_src_dir = './Voice_typer_update'
                root_dst_dir = './'
                for src_dir, dirs, files in os.walk(root_src_dir):
                    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    for file_ in files:
                        src_file = os.path.join(src_dir, file_)
                        dst_file = os.path.join(dst_dir, file_)
                        if os.path.exists(dst_file):
                            # in case of the src and dst are the same file
                            if os.path.samefile(src_file, dst_file):
                                continue
                            os.remove(dst_file)
                        shutil.move(src_file, dst_dir)
                        print("Update of voice typer succesful")


    except Exception:
        pass
else:
    print("please connect to internet")


