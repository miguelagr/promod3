#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import hashlib
import time
import psycopg2
import sys
import binascii



def genera_bd(fname,tabla,algo):
    """
    Genera la base de datos con todos los hashes de cada cadena de un archivo de entrada
    Argumento:
        Nombre del archivo donde se sacan las cadenas en claro (str)
        Nombre de la tabla (str)
    Salida:
        None
    """
    conn = psycopg2.connect("dbname=monitoreo user=root password=hola123")
    cur = conn.cursor()
    cmd = "select (LOWER(tablename)) from pg_tables where schemaname like 'public' and tablename like LOWER('%s')" % (tabla)
    cur.execute(cmd)
    if cur.fetchone() is None:
        cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, plain varchar%s);" % (tabla, ', "%s" varchar' * len(algo) % tuple(algo)))
	conn.commit()
        cmd = "INSERT INTO %s(plain, %s) VALUES ('%s', %s);" % (tabla, ('"%s",' * len(algo) % tuple(algo))[:-1], p, ("'%s'," * len(mh) % tuple(mh))[:-1])
        cur.execute(cmd)
	conn.commit()
	cur.close()
	conn.close()

def busca_hash(tabla,digest,algo):
    """
    Busca el texto en claro que corresponde al hash de la entrada
    Argumentos:
        Tabla de busqueda (str)
        Cadena del digest en formato hexadecimal (str)
        Algoritmos posibles para el digest (str[])
    Salida:
        Texto en claro correspondiente al hash de entrada (str[])
    """
    plain = []
    disponibles = []
    conn = psycopg2.connect("dbname=monitoreo user=root password=hola123")
    cur = conn.cursor()
    cmd = "select (column_name) from information_schema.columns where LOWER(table_name) like LOWER('%s')" % (tabla)
    cur.execute(cmd)
    al = cur.fetchone()
    while al:
        disponibles.append(al[0])
        al = cur.fetchone()
    return plain

def db_con(fname='',tabla='',algo=''):
    """
    Genera la base de datos con todos los hashes de cada cadena de un archivo de entrada
    Argumento:
        Nombre del archivo donde se sacan las cadenas en claro (str)
        Nombre de la tabla (str)
    Salida:
        None
    """
    conn = psycopg2.connect("dbname=monitoreo user=root password=hola123")
    cur = conn.cursor()
    cmd = "select (LOWER(tablename)) from pg_tables where schemaname like 'public'"
    cur.execute(cmd)
    al = cur.fetchone()
    while al:
        print al
        al = cur.fetchone()
    cur.close()
    conn.close()

def ChartGen(n_groups=0,xlabel='',ylabel='',title='',data=[],Lticks=()):
    opacity = 0.4
    b_width = 0.25
    ind = range(n_groups)
    fig, ax = plt.subplots()
    error_config = {'ecolor': '0.3'}
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ticks = [x + b_width / 2 for x in ind]
    ax.set_xticks(ticks)
    ax.set_xticklabels(Lticks)
    ax.legend()
    ax.bar(ticks,data,label='Algo')
    plt.savefig('Prueba.png')# Credit: Josh Hemann

#ChartGen(5,'hola','hola','tit',[1,2,1,1,1],('a','b','c','d','e'))
db_con()

#n_groups = 5
#xlabel = 'Grupos'
#ylabel = 'Valor'
#title = 'Prueba'
#means_men = (20, 35, 30, 35, 27)
#std_men = (2, 3, 4, 1, 2)
#means_women = (25, 32, 34, 20, 25)
#std_women = (3, 5, 2, 3, 3)
#fig, ax = plt.subplots()
#ind = range(n_groups)
#b_width = 0.25
#opacity = 0.4
#error_config = {'ecolor': '0.3'}
#ax.set_xlabel(xlabel)
#ax.set_ylabel(ylabel)
#ax.set_title(title)
#ticks = [x + b_width / 2 for x in ind]
#ax.set_xticks(ticks)
#ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
#ax.legend()
#ax.bar(ticks,[2,3,2,2,5],label='Algo')
#plt.savefig('Prueba.png')# Credit: Josh Hemann
