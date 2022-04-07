import datetime
import shutil
from datetime import date
import glob

path = '/backup'

src_backup_dir = '/redmine'
dst_backup = '/backup'

try:
    shutil.copytree(src_backup_dir,dst_backup)
    print("File copied succesfully")

except shutil.SameFileError:
    print("File does not exist or src and dst represents the same files ")
except:
    print("Error occurred while copying file")
