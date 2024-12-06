"""
Code pour convertir des fichiers Verilog en VHDL, générer un test bench
Loïc PAGNON
29/11/2024
A faire :
"""

from Verilog_VHDL import conversion
from TB import testbench_generation

conversion()

while input("Voulez-vous générer un test bench avec ceci ? Y/N  ") != "Y" or "N":
    if input("Voulez-vous générer un test bench avec ceci ? Y/N  ") == "Y":
        testbench_generation()
        