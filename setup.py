import os
import db_control as db


class setup():
    def __init__(self):
        self.install_pandas()
        # self.intall_tkinter()
        # self.crear_db_and_pickle()

    def install_pandas(self):
        os.system('pip install pandas')


    def intall_tkinter(self):
        os.system('pip install python-tk')


    def crear_db_and_pickle(self):
        db.new_db("control_horario")
        db.save_pickle({'fecha': 0, 'hora_entrada': 0}, 'C:/Users/imdt/Documents/control_horario', 'temporal_data')


if __name__ == '__main__':
    installer = setup()


