import pandas
import math

import db_control as db

# Función que lee la base de datos y añade columnas que se necesitarán
def ajust_data():
    datos_db = db.get_all_data('control_horario', 'tabla_control')
    datos_db["fecha"]=pandas.to_datetime(datos_db["fecha"], dayfirst=True, yearfirst=False)
    datos_db["horas_diarias"]=pandas.to_datetime(datos_db["horas_diarias"], dayfirst=True, yearfirst=False)
    datos_db['month'] = datos_db['fecha'].dt.month
    datos_db['year'] = datos_db['fecha'].dt.year
    datos_db['day'] = datos_db['fecha'].dt.day
    datos_db['horas'] = datos_db['horas_diarias'].dt.hour
    datos_db['minutos'] = datos_db['horas_diarias'].dt.minute

    return datos_db

def meses_db(year):
    datos_db = ajust_data()

    datos_por_year = pandas.DataFrame()
    for i in range(len(datos_db)):
        if datos_db.loc[i,'year'] == int(year):
            datos_por_year = datos_por_year.append(datos_db.loc[i])

    meses_df=datos_por_year.groupby('month').first()
    meses_df.reset_index(inplace=True)
    meses = []
    for i in range(len(meses_df)):
        meses.append(meses_df.loc[i,'month'])
    
    return meses

def years_db():
    datos_db = ajust_data()
    
    years_df=datos_db.groupby('year').first()
    years_df.reset_index(inplace=True)
    years = []
    for i in range(len(years_df)):
        years.append(years_df.loc[i,'year'])
    
    return years

def generate_excel(datos_a_generar, year, mes):
    if mes is None:
        excel_name = 'Datos_totales_' + str(year)
    else:
        excel_name = 'Datos_' +  str(nombre_meses(mes)) + '_' + str(year)
    
    horas, minutos = suma_horas_totales(datos_a_generar)
    tiempo = str(int(horas)) + ':' + str(int(minutos))

    datos_a_generar.loc[len(datos_a_generar),'total_trabajado'] = tiempo

    # datos_a_generar['total_trabajado'] = tiempo

    # h_trabajadas = pandas.DataFrame([tiempo], columns = ['total_trabajado'])   
    # datos_a_generar.append(h_trabajadas)
    # df.drop(['B', 'E'], axis='columns', inplace=True)
    if mes is None:
        datos_a_generar.drop(['day', 'horas', 'minutos','month','year', 'index'], axis='columns', inplace=True)
    else:
        datos_a_generar.drop(['day', 'horas', 'minutos','month','year', 'level_0', 'index'], axis='columns', inplace=True)

    datos_a_generar.to_excel( str(excel_name) + '.xlsx', sheet_name= excel_name)


def suma_horas_totales(datos_db):
    def suma_horas_df(datos_df):
        horas = 0
        for i in range(len(datos_df)):
            horas = horas + datos_df.loc[i,'horas']
        return horas

    def suma_min_df(datos_df):
        horas = 0
        minutos = 0
        for i in range(len(datos_df)):
            minutos = minutos + datos_df.loc[i,'minutos']

        horas = minutos / 60
        minutos, horas = math.modf(horas)
        minutos = minutos / 0.01666666667

        return horas, minutos

    horas_totales = suma_horas_df(datos_db)
    horas_min, minutos_totales = suma_min_df(datos_db)

    horas_totales = horas_totales + horas_min
    print('El total trabajado es ' + str(horas_totales) + ' horas y ' + str(minutos_totales) + ' minutos' )
    return horas_totales, minutos_totales

def get_year(year):
    datos_db = ajust_data()
    datos_por_year = pandas.DataFrame()
    for i in range(len(datos_db)):
        if datos_db.loc[i,'year'] == int(year):
            datos_por_year = datos_por_year.append(datos_db.loc[i])

    datos_por_year=datos_por_year.sort_values('month')
    datos_por_year.reset_index(inplace=True)
    return datos_por_year

def get_mes(datos_por_year, mes):
    datos_por_mes = pandas.DataFrame()
    for i in range(len(datos_por_year)):
        if datos_por_year.loc[i, 'month'] == int(mes):
            datos_por_mes = datos_por_mes.append(datos_por_year.loc[i])
    
    datos_por_mes=datos_por_mes.sort_values('day')
    datos_por_mes.reset_index(inplace=True)
    return datos_por_mes

def nombre_meses(num_mes):
    if num_mes == 1:
        return 'Enero'
    elif num_mes == 2:
        return 'Febrero'
    elif num_mes == 3:
        return 'Marzo'
    elif num_mes == 4:
        return 'Abril'
    elif num_mes == 5:
        return 'Mayo'
    elif num_mes == 6:
        return 'Junio'
    elif num_mes == 7:
        return 'Julio'
    elif num_mes == 8:
        return 'Agosto'
    elif num_mes == 9:
        return 'Septiembre'
    elif num_mes == 10:
        return 'Octubre'
    elif num_mes == 11:
        return 'Noviembre'
    elif num_mes == 12:
        return 'Diciembre'
    else:
        return '__Mes__'


