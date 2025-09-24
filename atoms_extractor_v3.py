# Crear las listas necesarias para convertir mi archivo PDB en TSV
a_number = []
atom = []
Residue = []
r_number = []
x = []
y = []
z = []
element = []

# Nombre del archivo PDB
PDB_file = 'TMC1.pdb'

# Abrir el archivo línea por línea
with open(PDB_file, 'r') as f:
    for line in f:
        if line.startswith('ATOM'):
            line = line.strip().split()  # dividir en columnas

            # agregar valores a cada lista
            a_number.append(line[1])
            atom.append(line[2])
            Residue.append(line[3])
            r_number.append(line[5])
            x.append(line[6])
            y.append(line[7])
            z.append(line[8])
            element.append(line[11])

# Agrupar todas las listas
big_list = [element, a_number, atom, Residue, r_number, x, y, z]

# Guardar en TSV
with open('TSV_file.tsv', 'w') as f:  # usar 'w' para sobrescribir
    # encabezado
    f.write('\t'.join(['elemento', 'N.atomo', 'atomo', 'Residuo', 'N.Residuo', 'x', 'y', 'z']) + '\n')
    # filas de datos
    for fila in zip(*big_list):
        f.write('\t'.join(map(str, fila)) + '\n')



