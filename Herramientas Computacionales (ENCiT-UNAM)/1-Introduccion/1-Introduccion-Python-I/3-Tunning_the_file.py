# 2-how_a_python_code_looks_like.py
# Jonathan Urrutia
# Las modified: 2022-01-26

# To know the basic we will examine the following code, while commenting it

# In python a variable can hold different kind of data: integers, floats, strings, etc.
# This is done authomatically by python, that is, you do not have to tell it: There is
# no declaration of variables. We can define them as and when we want.

principal = 1000	# Initial amount
rate = 0.05		# Initial rate
num_years = 5		# Number of years
 

print( "Let's print the outcome")
year = 1
# This is a while-loop. It controlls the flow of the instructions based on a condition
# The instructions inside the loop are those with identation after the condition.
while year <= num_years:			# While year is smaller than num_years, then:
	principal = principal * (1 + rate)	# Multiply principal by (1+rate) and then assign to this varable the new values just calculated
	print( year, principal)			# Print to the user what you've got
	year += 1				# Incirease the value of year by 1 unit

# A new line ends and instruction but we can  write them in a single line by separating
# them with a semicolon (;)

print ("\n Now, with no new lines")
year = 1; principal = 1000
while year <= num_years:
	principal = principal * (1 + rate); print( year, principal); year += 1

# Which is easier to read?

print("\nLet's make the output look better:")
year = 1
principal = 1000

print("Year\tPrincipal\tRate\n--------------------")
while year <= num_years:
	principal = principal * (1 + rate)
	print("%3d\t %0.2f\t%0.5f" % (year, principal,rate))
	year += 1

