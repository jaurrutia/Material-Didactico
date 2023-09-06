# Commenting_changes.py
# Author
# Las modified: 

# La idea es que hagas de este código algo más legible para otros usuarios y que
# lo hagas más claro, mencionando los cambios siguientes:
# 	1 - Cambia los parámetros iniciales, en particular di qye num_years es tu edad actual
#	2 - Comenta qué ocurre en el ciclo while
#	3 - Repite el procedimiento pero ahora vas a imprimir en la pantalla una tabla con 
#	    encabezados la información.


principal = 1000	
rate = 0.05		
num_years = 5		
 
year = 1
while year <= num_years:
	principal = principal * (1 + rate)
	print( year, principal)
	year += 1
