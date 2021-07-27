import os
import time

"""The files and directories to be backed up are specified in a list
Example on Windows OS: source = ['"C:\\My Documents"', 'C:\\Code']
Example on Unix: source = ['/Users/nome/Documents'] 
 """
source = '/home/fabio/Pictures'

"""The backup must be stored  in a  main backup  directory
 Example Windows: target_dir ='E:\\Backup'
 Example Unix: target_dir='/Users/nome/Backup"""

target_dir = '/home/fabio/backup'

"""The files are backed up into a zip file. The name of the zip archive
 is the current  date and time.
 Example: target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'"""

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

"""Create  target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
"""

if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

"""the files are backed up into a zip file. The current day is
the name  of the subdirectory."""
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if isn't already  there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory.',today)


"""Use the zip command to put the files in zip archive
Example:
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))"""

zip_command = "zip -r {0} {1}".format(target, ''.join(source))

# Run the backup
print("Zip command is: ")
print(zip_command)
print("Running")

if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print('Backup Failed')