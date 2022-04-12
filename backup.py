from datetime import date
import shutil
import os
import sys

mysql_user = 'redmine'
mysql_password = 'redmine2022'
src_back_dir = '/redmine'
dst_backup_dir = '/backup'
mysql_file = 'red'


try:
    today = date.today()
    date_format = today.strftime("%d_%b_%y_")
    dst_backup_dir = dst_backup_dir + date_format
    mysql_file_name = mysql_file + date_format + ".sql"
    mysql_backup = os.system("cd %s && mysql - u %s -p %s --databases redmine_db %s").format(dst_backup_dir,mysql_user,mysql_password,mysql_file_name) 
    shutil.copytree(src_back_dir, dst_backup_dir)
    shutil.copy(mysql_file_name,dst_backup_dir)
    print("File copied succesfully")


except shutil.SameFileError:

    print("File does not exist or src and dst represents the same files")

except:

    print("Error occurred while copying file")  
