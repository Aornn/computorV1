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
    if equation.find('*X^' + str(p)) == -1:
        p0 = "0"
        return p0
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
power_2 = eval(isole_p(2)) #a
power_1 = eval(isole_p(1)) #b
power_0 = eval(isole_p(0) + neutre)
if (power_1 >= 0):
    power_1 = "+" + str(power_1)
if (power_2 >= 0):
    power_2 = "+" + str(power_2)


delta = (float(power_1) * float(power_1)) - (4 * float(power_2) * float(power_0))
if (delta > 0 and eval(power_2) != 0):
    print "delta : " + str(delta) +" > 0"
    b = float(power_1) * -1
    x_prime = (b + delta**0.5) / (2 * float(power_2))
    x_seconde =(b - delta**0.5) / (2 * float(power_2))
    print "les solutions sont : " + str(x_prime) + " et " + str(x_seconde)
    tot = str(power_0)  + str(power_1) +"X"+str(power_2)+"X^2"
    print "forme reduite : " + tot + " = 0"
elif (delta == 0):
    print "delta = 0"
    tot = str(power_0)  + str(power_1) +"X"+str(power_2)+"X^2"
    print "forme reduite : " + tot + " = 0"
elif (delta < 0):
    print "delta = " + str(delta) + " < 0"
    print "Pas de solution dans R"
if (eval(power_2) == 0):
    print "Degre 1"
    tot1 = str(power_0)  + str(power_1) +"X"
    ret = (float(power_0) * -1) / float(power_1)
    print "Forme reduite : " + str(tot1)
    print "Resultat :" + str(ret)
