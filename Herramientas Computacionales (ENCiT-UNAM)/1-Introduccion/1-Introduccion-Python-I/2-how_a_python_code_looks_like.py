# 2-how_a_python_code_looks_like.py
# Jonathan Urrutia
# Las modified: 2022-01-26
#
# Calcula e imprime el aumento en una cuenta de banco con una taza fija de interés.
#

# Para familiarizarnos con Python comentemos este archivo y modifiquémoslo

principal = int(input("Dame un valor inicial de dinero con numeros:\n"))	# Cantidad inicial
rate = 0.05		# Initial rate
num_years = 5		# Number of years
 
year = 1
while year <= num_years:
	principal = principal * (1 + rate)
	print( year, principal)
	year += 1


# El cálculo mostrado con print se muestra en la línea de comando. Si esta información me es útil, 
# es conveniente ponerla en un archivo de texto (.txt, .dat, .csv)
# Para hacer esto, empleamos los siguientes comandos en la terminal:
#
# python3 file_name.py > output.txt
# python3 file_name.py >> output.txt
#
# ¿Cuál es la diferencia entre estos comandos? Juega con ellos
#
