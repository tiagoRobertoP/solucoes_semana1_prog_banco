# This Python file uses the following encoding: utf-8
import os, sys

salario = float(input('Digite seu salario: '))
gratificao = salario * 0.05
imposto = salario * 0.07
print("Salario Final é " + str(salario + gratificao - imposto))