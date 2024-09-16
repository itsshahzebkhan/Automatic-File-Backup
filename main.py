# step 1 - to start this project you need to install PyCharm community edition or VS Code
# step 2 - you need to install a package from your terminal - "schedule" and then import it as shown below
# step 3 - you ned to import four packages "os, shutil, datetime, time" which are already installed in PyCharm and VS Code
# step 4 - start coding


import os
import shutil
import datetime
import schedule
import time


source_dir = "here, type the source of the folder"
destination_dir = "here, type the destination of the folder"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("here, type the time that you want to choose").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)