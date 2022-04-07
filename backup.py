from datetime import date
import shutil

src_back_dir = '/redmine'
dst_backup_dir = '/backup'

try:
    today = date.today()
    date_format = today.strftime("%d_%b_%y_")
    dst_backup_dir = dst_backup_dir + date_format
    shutil.copytree(src_back_dir,dst_backup_dir)
    print("File copied succesfully")

except shutil.SameFileError:
    
    print("File does not exist or src and dst represents the same files")

except:
    
    print("Error occurred while copying file")        
