"""! @brief Janela inicial do jogo Chrome TRex"""
##
# @file sensor.py
#
# @brief
# Arquivo com funcoes de leitura do arduino
#
# @author Claudio Rogerio 19.11.2021
#
# @section TODO
#
# @section MAKED

import pygame
import numpy as np
import serial
import time


##get_data_arduino( '/dev/ttyUSB0', 9600 )
# [0] - Info do sensor
# [1] - Dados do sensor

def start_sensor( port, ciclos ):
    sensor = serial.Serial( port, ciclos, timeout=0.1 )
    time.sleep(1)
    return sensor

def get_data_arduino( sensor ):

    serial = sensor.readline()
    serial = serial.decode()

    if serial != '':
        return float( serial.split()[1] )
    else:
        return -1.0
