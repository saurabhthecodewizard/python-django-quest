import zipfile
import os
import shutil

f = open('one.txt', 'w+')
f.write('First File')
f.close()

f = open('two.txt', 'w+')
f.write('Second File')
f.close()

file = zipfile.ZipFile('compressed.zip', 'w')

file.write('one.txt', compress_type=zipfile.ZIP_DEFLATED)
file.write('two.txt', compress_type=zipfile.ZIP_DEFLATED)

file.close()

extracted = zipfile.ZipFile('compressed.zip', 'r')
extracted.extractall('extracted')

print(os.listdir())

print(shutil.make_archive('example', 'zip', os.getcwd()))

print(os.listdir())

shutil.unpack_archive('example.zip', 'unpacked', 'zip')

print(os.listdir())
