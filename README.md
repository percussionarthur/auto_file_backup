# auto_file_backup

Daily Folder Backup Script

This Python script automates the daily backup of a specified folder to a backup directory. It schedules the task using the schedule library, with each backup stored in a subfolder named by the current date.

Requirements:

- Python 3

Required Libraries:

- os (comes pre-installed with Python)
- shutil (comes pre-installed with Python)
- datetime (comes pre-installed with Python)
- schedule (install with pip install schedule)
- time (comes pre-installed with Python)

Functions:

1. Backup Function
   - **`copy_folder_to_directory()`**: Copies the contents of the source folder to a date-named subfolder in the backup directory.
   - Uses the current date to create a subfolder in the destination directory.

2. Directory Setup
   - **Source Directory**: Path to the folder to be backed up.
   - **Destination Directory**: Path to the folder where backups will be stored.

3. Scheduling
   - **`schedule.every().day.at("16:15").do(...)`**: Uses the `schedule` library to run the backup function every day at a specified time.

4. Execution
   - **Initial Run**: Executes the backup immediately when the script starts.
   - **Continuous Monitoring**: Keeps the script running, checking every 60 seconds for scheduled tasks.
