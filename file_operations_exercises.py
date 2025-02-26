# Exercise 1: Count occurrences of "ERROR" in a log file
def count_errors_in_log(log_file_path):
    """Count occurrences of the word 'ERROR' in a log file."""
    error_count = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                error_count += line.count('ERROR')
        
        print(f"Found {error_count} errors in {log_file_path}")
        return error_count
    except FileNotFoundError:
        print(f"Error: File {log_file_path} not found.")
        return -1
    except Exception as e:
        print(f"Error reading log file: {str(e)}")
        return -1

# Exercise 2: Create a report of down servers from a CSV
import csv

def create_down_server_report(input_csv, output_report):
    """
    Read server status from CSV and create a report of down servers.
    
    Expected CSV format:
    hostname,ip,status
    server1,192.168.1.1,up
    server2,192.168.1.2,down
    """
    down_servers = []
    
    try:
        # Read the CSV file
        with open(input_csv, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['status'].lower() == 'down':
                    down_servers.append(row)
        
        # Write the report
        with open(output_report, 'w') as report_file:
            report_file.write("DOWN SERVERS REPORT\n")
            report_file.write("=================\n\n")
            
            if down_servers:
                for server in down_servers:
                    report_file.write(f"Hostname: {server['hostname']}\n")
                    report_file.write(f"IP Address: {server['ip']}\n")
                    report_file.write(f"Status: {server['status']}\n")
                    report_file.write("-----------------\n")
                report_file.write(f"\nTotal down servers: {len(down_servers)}")
            else:
                report_file.write("No servers are currently down.")
        
        print(f"Report created at {output_report}")
        return True
    except Exception as e:
        print(f"Error creating report: {str(e)}")
        return False

# Exercise 3: Backup Python files to a zip archive
import os
import zipfile
from datetime import datetime

def backup_python_files(directory_path):
    """Backup all .py files in a directory to a date-stamped zip file."""
    today = datetime.now().strftime("%Y%m%d")
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

# Example usage
if __name__ == "__main__":
    # Count errors
    count_errors_in_log("example_log.txt")
    
    # Create server report
    create_down_server_report("servers.csv", "down_servers_report.txt")
    
    # Backup Python files
    backup_python_files("C:\\Users\\techs\\Documents\\Disha Computer Institute\\Python For DevOps")