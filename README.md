# PDB_to_TSV

# Conversión de archivos PDB a TSV

# Este proyecto contiene un script en Python que transforma un archivo en formato PDB (Protein Data Bank) a un archivo TSV (Tab-Separated Values).
# El objetivo es extraer información relevante de los átomos de una molécula, como:

# 1.Tipo de átomo
# 2.Residuo al que pertenece
# 3.Número de residuo
# 4.Coordenadas x, y, z
# 5.Elemento químico

# y organizarla en una tabla fácil de leer y analizar.

# Funcionamiento

# El programa abre un archivo .pdb y lo lee línea por línea.
# Selecciona únicamente las líneas que empiezan con ATOM.
# Extrae los campos de interés: número de átomo, tipo de átomo, residuo, número de residuo, coordenadas y elemento.
# Organiza los datos en un archivo .tsv con columnas separadas por tabulación (\t).

# Ejemplo de entrada (PDB simplificado)
#   ATOM      1  N   MET A   1      38.428  13.230   9.947  1.00 67.62           N
#   ATOM      2  CA  MET A   1      37.907  12.074   9.148  1.00 67.62           C

# Ejemplo de salida (TSV)
# elemento	N.atomo	atomo	Residuo	N.Residuo	      x	     y	    z
#     N	        1	    N	    MET	    1	        38.428	13.230	9.947
#     C	        2	    CA	  MET	    1	        37.907	12.074	9.148

# Requisitos
#  Python 3.x
#  No requiere librerías externas
