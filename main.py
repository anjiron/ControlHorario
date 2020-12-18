import datetime
import pandas


import db_control as db
import gui


def complete_check(hora_salida):
    if hora_salida == '0':
        return False
    else:
        return True


def save_day(fecha, hora_entrada, hora_salida, horas_diarias):
    entrada_db = (fecha, hora_entrada, hora_salida, horas_diarias)
    db.insert_data_db("control_horario", entrada_db)


def horas_trabajadas(string_entrada, string_salida):

    hora_entrada = datetime.datetime.strptime(string_entrada, "%H:%M:%S")
    hora_salida = datetime.datetime.strptime(string_salida, "%H:%M:%S")

    horas = hora_salida - hora_entrada
    return str(horas)


# db.new_db("control_horario")
# db.save_pickle({'fecha': 0, 'hora_entrada': 0}, 'C:/Users/imdt/Documents/control_horario', 'temporal_data')


fecha, hora_entrada, hora_salida = gui.run_gui()

if complete_check(hora_salida) is False:
    temp_data = {'fecha': fecha, 'hora_entrada': hora_entrada}
    db.save_pickle(temp_data, 'C:/Users/imdt/Documents/control_horario', 'temporal_data')
elif complete_check(hora_salida) is True:
    horas_diarias = horas_trabajadas(hora_entrada, hora_salida)
    save_day(fecha, hora_entrada, hora_salida, horas_diarias)
else:
    print('ERROR')

