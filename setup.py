
import os
import sys
import shutil

import db_control as db


class setup():
    def __init__(self):
        abs_path = os.path.split(os.path.abspath(__file__))
        path = abs_path[0]
        os.mkdir(str(path) + '\excel')    

        self.install_pandas()
        self.install_pyinstaller()
        self.install_openpyxl()
        self.crear_db_and_pickle(path)
        self.crear_exe_main(path)

    def install_pandas(self):
        os.system('pip install pandas')

    def install_pyinstaller(self):
        os.system('pip install pyinstaller')

    def install_openpyxl(self):
        os.system('pip install openpyxl')

    def crear_db_and_pickle(self, path):
        db.new_db("control_horario")
        db.save_pickle({'fecha': 0, 'hora_entrada': 0}, path, 'temporal_data')

    def move_files(self, file_name, new_path, old_path):
        sistema = sys.platform
        if sistema == 'linux':
            os.system('sudo cp -R ' + str(old_path) + str(file_name) + " " + str(new_path))
        elif sistema == 'win32':
            os.system('MOVE ' + str(old_path) + str(file_name) + " " + str(new_path))


    def crear_exe_main(self, path):
        old_path = str(path) + '\dist'
        os.system('pyinstaller --windowed --onefile main.py')
        self.move_files('\main.exe', path, old_path)
        shutil.rmtree(old_path)
        shutil.rmtree(str(path) + '/build')
        os.remove(str(path) + '/main.spec')


if __name__ == '__main__':
    installer = setup()


