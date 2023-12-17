import os
import shutil
import send2trash

f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

project_path = "D:\\workspace\\work\\repositories\\python-django-quest\\"

print(os.getcwd())
print(os.listdir())
print(os.listdir(project_path))

# shutil.move("practice.txt", "D:\\workspace\\work\\")

# os.unlink(path) which deletes a file at the path your provide
# os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
# shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.

send2trash.send2trash('practice.txt')

for folder, sub_folders, files in os.walk(project_path):
    print()
    print()
    print(f'Currently looking at {folder}')
    print()
    print('Sub-folders are as follows:-')
    for sub_folder in sub_folders:
        print(f'\t Sub-folder: {sub_folder}')
    print()
    print('The files are:-')
    for file in files:
        print(f'\t\t File: {file}')

