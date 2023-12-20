import os
import pystray
from pystray import MenuItem
from PIL import Image, ImageTk
from connect_psql import db_name
import datetime

m = []

def quit_tray(icon, item):
    icon.stop()

def save_dump(db_name_):
    def save_dump_db(icon, item):
        
        date = datetime.datetime.now().strftime('%d_%m')
        os.system("pg_dump "+ db_name_ +"> /Users/admin/Desktop/"+ db_name_+ "_" + date +".sql")
    
    return save_dump_db

for i in range(0, len(db_name)):
    m.append(MenuItem(db_name[i], save_dump(db_name[i])))

m.append(MenuItem('quit', quit_tray))

image = Image.open("ico/ico.png")
icon = pystray.Icon(
    "SaveDump",
    menu=m,
    icon=image)

icon.run()



