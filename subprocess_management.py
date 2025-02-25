# For Unix/Linux :- 

import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

# For Windows :- 
import subprocess
result = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
print(result.stdout)

# For cross-platform compatibility :- 

import subprocess
import platform

if platform.system() == 'Windows':
    result = subprocess.run('dir', shell=True, capture_output=True, text=True)
else:
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    
print(result.stdout)