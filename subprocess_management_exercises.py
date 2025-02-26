import subprocess
import threading
import time
import shlex
import sys
import os
import platform
from datetime import datetime

# Exercise 1: System health check script
def system_health_check():
    """Run system health checks using various shell commands."""
    print("SYSTEM HEALTH CHECK")
    print("===================")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Cross-platform hostname check
    try:
        if hasattr(os, 'uname'):
            hostname = os.uname().nodename
        else:
            # For Windows
            hostname = platform.node()
        print(f"Hostname: {hostname}")
    except Exception as e:
        print(f"Error getting hostname: {str(e)}")
    
    print("===================\n")
    
    # Check disk space
    print("DISK SPACE:")
    try:
        if sys.platform == 'win32':
            result = subprocess.run(['wmic', 'logicaldisk', 'get', 'deviceid,freespace,size'], 
                                  capture_output=True, text=True, check=True)
        else:
            result = subprocess.run(['df', '-h'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.SubprocessError as e:
        print(f"Error checking disk space: {str(e)}")
    
    # Check memory usage
    print("MEMORY USAGE:")
    try:
        if sys.platform == 'linux':
            result = subprocess.run(['free', '-h'], capture_output=True, text=True, check=True)
            print(result.stdout)
        elif sys.platform == 'darwin':  # macOS
            result = subprocess.run(['vm_stat'], capture_output=True, text=True, check=True)
            print(result.stdout)
        elif sys.platform == 'win32':
            result = subprocess.run(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize'],
                                  capture_output=True, text=True, check=True)
            print(result.stdout)
    except subprocess.SubprocessError as e:
        print(f"Error checking memory usage: {str(e)}")
    
    # Check CPU load
    print("CPU LOAD:")
    try:
        if sys.platform == 'linux':
            result = subprocess.run(['uptime'], capture_output=True, text=True, check=True)
            print(result.stdout)
            
            # More detailed CPU info
            try:
                result = subprocess.run('top -bn1 | grep Cpu', 
                                     shell=True, capture_output=True, text=True)
                print(result.stdout)
            except:
                pass
        elif sys.platform == 'darwin':  # macOS
            result = subprocess.run(['sysctl', '-n', 'vm.loadavg'],
                                  capture_output=True, text=True, check=True)
            print(f"Load Average: {result.stdout}")
        elif sys.platform == 'win32':
            result = subprocess.run(['wmic', 'cpu', 'get', 'loadpercentage'],
                                  capture_output=True, text=True, check=True)
            print(result.stdout)
    except subprocess.SubprocessError as e:
        print(f"Error checking CPU load: {str(e)}")
    
    # Check running processes
    print("TOP PROCESSES:")
    try:
        if sys.platform == 'linux':
            result = subprocess.run('ps aux --sort=-%cpu | head -10',
                                 shell=True, capture_output=True, text=True)
            print(result.stdout)
        elif sys.platform == 'darwin':  # macOS
            result = subprocess.run('ps -Ao pid,comm,%cpu --sort=-%cpu | head -10',
                                 shell=True, capture_output=True, text=True)
            print(result.stdout)
        elif sys.platform == 'win32':
            result = subprocess.run(['tasklist', '/v', '/fi', 'STATUS eq running'],
                                  capture_output=True, text=True, check=True)
            print(result.stdout[:500])  # Limit output
    except subprocess.SubprocessError as e:
        print(f"Error checking running processes: {str(e)}")
    
    print("\nHEALTH CHECK COMPLETE")

# Example usage
if __name__ == "__main__":
    # Run system health check
    system_health_check()