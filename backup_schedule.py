import os
import zipfile
from datetime import datetime
import schedule
import time

def backup_python_files(directory_path):
    """Backup all .py files in a directory to a date-stamped zip file."""
    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"python_backup_{today}.zip"
    
    try:
        # Create a zip file
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Walk through directory
            for root, _, files in os.walk(directory_path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        # Add file to zip with its relative path
                        arcname = os.path.relpath(file_path, directory_path)
                        zipf.write(file_path, arcname=arcname)
                        print(f"Added {file_path} to backup")
            
            print(f"Backup created successfully: {zip_filename}")
        return zip_filename
    except Exception as e:
        print(f"Error creating backup: {str(e)}")
        return None

def start_scheduler(directory_path, interval_type="minutes", interval_value=5):
    """
    Start the backup scheduler with specified interval.
    
    Args:
        directory_path: Path to backup
        interval_type: "minutes" or "days"
        interval_value: Number of time units between backups
    """
    if interval_type.lower() == "minutes":
        schedule.every(interval_value).minutes.do(backup_python_files, directory_path)
        print(f"Scheduled backups to run every {interval_value} minutes")
    elif interval_type.lower() == "days":
        schedule.every(interval_value).days.do(backup_python_files, directory_path)
        print(f"Scheduled backups to run every {interval_value} days")
    else:
        print(f"Invalid interval type: {interval_type}. Using minutes as default.")
        schedule.every(interval_value).minutes.do(backup_python_files, directory_path)
    
    # Run the backup once immediately
    print("Running initial backup...")
    backup_python_files(directory_path)
    
    # Keep the script running
    print("Backup scheduler is running. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Backup scheduler stopped by user.")

if __name__ == "__main__":
    # Configuration
    directory_to_backup = "C:\\Users\\techs\\Documents\\Disha Computer Institute\\Python For DevOps"
    
    # Set to "minutes" for 5-minute intervals or "days" for 5-day intervals
    backup_interval = "minutes"  # or "days"
    backup_value = 2
    
    # Start the scheduler
    start_scheduler(directory_to_backup, backup_interval, backup_value)