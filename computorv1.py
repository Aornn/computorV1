#!/usr/bin/env python
import os
import re
import sys
import string
equation = sys.argv[1]
membre_second = ""
membre_premier = ""
a = ""
b = ""
c = ""
delta = ""

if (len(sys.argv) > 2):
    print "Trop d'arguments"
    sys.exit(0)
if (equation.count("=") != 1):
    print "Nombre de signes \'=\' incorrect"
    sys.exit(0)
equation = equation.replace(' ', '')
#equation = equation.replace('X^0', '1')
#equation = equation.replace('^', '**')
index = equation.find('=')
i = 0
while i < index:
    membre_premier += equation[i]
    i += 1
i = index + 1;
if (equation[i] == '-'):
    membre_second = '+'
    i = i +1
elif(equation[i] == '+'):
    membre_second = '-'
    i = i + 1
else:
    membre_second = '-'
while i < len(equation):
    if(equation[i] == '-'):
        membre_second += '+'
    elif (equation[i] == '+'):
        membre_second += '-'
    else:
        membre_second += equation[i]
    i += 1
equation = membre_premier + str(membre_second)
neutre = equation


def isole_p(p):
    i = 0
    indexp0 = []
    while i < len(equation):
        i = equation.find('*X^' + str(p), i)
        j = i-1
        if i != -1:
            p0 = ""
            while (j >0 and (equation[j] != '-' and equation[j] != '+')):
                p0 += equation[j]
                j -= 1
            p0 += equation[j]
            p0 = p0[::-1]
            indexp0.append(p0)
        else:
            break
        i += 4
    i = 0
    p0 = ""
    while (i < len(indexp0)):
        p0 += indexp0[i]
        global neutre
        neutre = neutre.replace( indexp0[i]+ '*X^' + str(p), '')
        i += 1
    return p0

power_0 = isole_p(0) #c
power_1 = isole_p(1) #b
power_2 = isole_p(2) #a
power_0 += neutre
power_0 = eval(power_0)
power_1 = eval(power_1)
power_2 = eval(power_2)
if (power_1 >= 0):
    power_1 = "+" + str(power_1)
if (power_2 >= 0):
    power_2 = "+" + str(power_2)
#print "partie 1 : " + str(float(power_1) * float(power_1))
#print "partie 2 : " + str(4 * float(power_2) * float(power_0))
delta = (float(power_1) * float(power_1)) - (4 * float(power_2) * float(power_0))

if (delta > 0):
    print "delta : " + str(delta) +" > 0"
    b = float(power_1) * -1
    x_prime = (b + racine(delta)) / (2 * float(power_2))
    x_seconde =(b - racine(delta)) / (2 * float(power_2))
    print "les solutions sont : " + x_prime + " et " + x_seconde
elif (delta == 0):
    print "delta = 0"
else:
    print "delta : " + str(delta) +" < 0"
    print "pas de solution"
tot = str(power_0)  + str(power_1) +"*X"+str(power_2)+"*X^2"
print "forme reduite : " + tot + " = 0"