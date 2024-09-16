import os
import shutil
import datetime
import schedule
import time

# define source and destination directories
# os.path.expanduser() expands ~ in the file paths
source_dir = os.path.expanduser("~/Documents/CompTIA/A+")
destination_dir = os.path.expanduser("~/Documents/CompTIA/backup")

def copy_folder_to_directory(source, dest):
    """this function copies the folder and appends the 
    current date as a subfolder in the destination directory
    """
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir) 
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")

# schedules the backup function to run daily at 16:15
schedule.every().day.at("16:15").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

copy_folder_to_directory(source_dir, destination_dir)

# keeps the script running and checking every 60 secondsto see if there are pending scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
