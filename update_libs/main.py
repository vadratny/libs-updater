import os
os.system('cd C:\Program Files\Python39\Lib\site-packages')
libs = os.listdir('C:\Program Files\Python39\Lib\site-packages')
for lib in libs:
    if ('.dist-info' or '.pth' or '.txt' or '.whl') in lib:
        libs.remove(lib)
for lib in libs:
    os.system(f'pip install --upgrade {lib}')