import tkinter as tk
import datetime
import datos
import os

import db_control as db

def run_gui():
    ventana = tk.Tk()
    ventana.title ("    ------- CONTROL HORARIO -------")
    ventana.geometry ("500x250+500+250")

    fecha = tk.StringVar(ventana)
    tk.Label(ventana, text = "Fecha:").pack()
    caja_fecha = tk.Entry(ventana, textvariable=fecha)
    caja_fecha.pack()

    hora_entrada = tk.StringVar(ventana)
    tk.Label(ventana, text = "Hora entrada:").pack()
    caja_hora_entrada = tk.Entry(ventana, textvariable=hora_entrada)
    caja_hora_entrada.pack()


    hora_salida = tk.StringVar(ventana)
    tk.Label(ventana, text = "Hora salida:").pack()
    caja_hora_salida = tk.Entry(ventana, textvariable=hora_salida)
    caja_hora_salida.pack()
    hora_salida.set('0')

    # fecha.trace("w", lambda *args: caja_fecha.config({"background": "#ffffff"}))
    # hora_entrada.trace("w", lambda *args: caja_hora_entrada.config({"background": "#ffffff"}))
    # hora_salida.trace("w", lambda *args: caja_hora_salida.config({"background": "#ffffff"}))

    def fecha_actual():
        actual = str(datetime.datetime.now().date())
        partes = actual.split("T")[0].split("-")
        convertida = "/".join(reversed(partes))
        fecha.set(convertida)

    def hora_actual_entrada():
        hora_inicio = datetime.datetime.now().time()
        hora_inicio_actual = str(hora_inicio.hour) + ':' + str(hora_inicio.minute) + ':00'
        hora_entrada.set(hora_inicio_actual)

    def hora_actual_salida():
        hora_fin = datetime.datetime.now().time()
        hora_fin_actual = str(hora_fin.hour) + ':' + str(hora_fin.minute) + ':00'
        hora_salida.set(hora_fin_actual)

    def recuperar_datos():
        abs_path = os.path.split(os.path.abspath(__file__))
        path = abs_path[0]
        data_recov = db.load_pickle(path, 'temporal_data')
        fecha.set(data_recov['fecha'])
        hora_entrada.set(data_recov['hora_entrada'])

    def guardar_salir():
        ventana.destroy()
    
    def excel(year, mes):
        datos_year = datos.get_year(year)

        if mes is None:
            datos_a_generar = datos_year
        else:
            datos_a_generar = datos.get_mes(datos_year, mes)

        datos.generate_excel(datos_a_generar, year, mes)

    def ventana_meses(year):
        w_meses = tk.Tk()
        w_meses.title ("------- MESES DE " + str(year) + " -------")
        w_meses.geometry ("500x250+500+250")
        meses = datos.meses_db(year)

        for i in range(len(meses)):
            texto_boton = 'Datos de ' + datos.nombre_meses(meses[i])
            tk.Button(w_meses, text=texto_boton, command=lambda mes = meses[i]:[excel(year, mes), w_meses.destroy()]).pack()
        
        nombre_boton = 'Datos totales de ' + str(year) 
        tk.Button(w_meses, text=nombre_boton, command=lambda:[excel(year, None), w_meses.destroy()]).pack()

        w_meses.mainloop()

    def ventana_years()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               :
        w_years = tk.Tk()
        w_years.title ("------- AÑOS -------")
        w_years.geometry ("500x250+500+250")
        years = datos.years_db()
        for i in range(len(years)):
            texto_boton = 'Datos de ' + str(years[i])                                             
            tk.Button(w_years, text=texto_boton, command = lambda year = years[i]:[ventana_meses(year)]).pack()
        
        w_years.mainloop()

    # Botones

    tk.Button (text = "Guardar", command=guardar_salir).pack()
                                        
    boton_fecha_actual = tk.Button (text = "Fecha actual", command=fecha_actual)
    boton_fecha_actual.place(x=80, y=20)
    boton_hora_inicio_actual = tk.Button (text = "Hora actual", command=hora_actual_entrada)
    boton_hora_inicio_actual.place(x=80, y=60)
    boton_hora_salida_actual = tk.Button (text = "Hora actual", command=hora_actual_salida)
    boton_hora_salida_actual.place(x=80, y=100)
    boton_rec = tk.Button (text ='Recuperar', command=recuperar_datos)
    boton_rec.place(x=10, y=20)
    boton_excel = tk.Button(text='Generar Excel', command=ventana_years)
    boton_excel.pack()

    ventana.mainloop()

    fecha_control = fecha.get()
    hora_entrada_control = hora_entrada.get()
    hora_salida_control = hora_salida.get()

    h_entrada = datetime.datetime.strptime(hora_entrada_control, "%H:%M:%S").time()
    if hora_salida_control == '0':
        h_salida = '0'
    else:
        h_salida = datetime.datetime.strptime(hora_salida_control, "%H:%M:%S").time()

    return fecha_control, str(h_entrada), str(h_salida)


# run_gui()