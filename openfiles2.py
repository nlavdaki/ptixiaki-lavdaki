
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


def appender(number):
    my_string = ''
    if number // 10 == 0:
        my_string = "00" + str ( number )
    elif number // 100 == 0:
        my_string = "0" + str ( number )
    else:
        my_string = str ( number )
    return my_string


key = str ( )
for x in range ( 1 , 367 ):
    if x != 22 and x != 23  and x != 24 and x !=111 :

        key = appender ( x )


        pathD = "C:/Users/Lavdi/Desktop/DIRECT_2016-2019/2016/DIR" + key + "16.DAT"
        pathG = "C:/Users/Lavdi/Desktop/GLB_2016-2019/2016/TOT" + key + "16.DAT"

        with open ( pathD , 'r' ) as D:
            datad = np.genfromtxt ( D , delimiter='' )
            time = datad[:,][1:,0]
            sza = datad[:,][1:,1]
            ID = datad[:,][1:,2]


            ID = ID[ID > 5]
            sza = sza[sza<85]

        with open (pathG, 'r') as G:
            datag = np.genfromtxt ( G , delimiter='' )
            IG = datag[:,][1:,2]

            IG = IG[IG>5]

            k=np.cos((sza*math.pi)/180)

            import array

            arrk =  []

            arrk.append ( k )

            diff = []

            diffuse = IG - np.multiply(ID,arrk)

            diff.append(diffuse)

            print(diff)
















