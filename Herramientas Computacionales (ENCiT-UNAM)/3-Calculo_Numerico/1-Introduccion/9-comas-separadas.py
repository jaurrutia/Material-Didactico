
import csv

print('Creemos un archivo de comas separadas:')
print('''with open('sample.csv', 'w', newline='') as csvfile:  # La w significa de write
    writer = csv.writer(csvfile)
    writer.writerow(['She Loves You', 'Sept 1963'])
    writer.writerow(['I Want to Hold Your Hand', 'Dec 1963'])
    writer.writerow(['Cant Buy Me Love', 'Apr 1964'])
    writer.writerow(['A Hard Days Night', 'July 1964'])
''')
with open('sample.csv', 'w', newline='') as csvfile:  # La w significa de write
    writer = csv.writer(csvfile)
    writer.writerow(['She Loves You', 'Sept 1963'])
    writer.writerow(['I Want to Hold Your Hand', 'Dec 1963'])
    writer.writerow(['Cant Buy Me Love', 'Apr 1964'])
    writer.writerow(['A Hard Days Night', 'July 1964'])

input('')

print('Y para leerlo:')
print('''with open('sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(*row, sep=', ')
''')
input('')
with open('sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(*row, sep=', ')

input('')


print('Podemos scar provecho de los diccionarios para trabajar con los CSV:')
print('''with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'result']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'John','last_name': 'Smith','result' : 54})
''')
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'result']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'John','last_name': 'Smith','result' : 54})
    writer.writerow({'first_name': 'Jane', 'result': 63, 'last_name': 'Lewis'})
    writer.writerow({'first_name': 'Chris', 'last_name': 'Davies','result' : 72})

input('')

print('''with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')

    for row in reader:
        print(row['first_name'], row['last_name'],row['result'])
''')
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')

    for row in reader:
        print(row['first_name'], row['last_name'],row['result'])
