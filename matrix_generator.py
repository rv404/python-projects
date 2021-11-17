# Program to generate a custom size matrix and
# fill each cell with a custom integer or character.

def matrix_generator():
  print('Custom Matrix Generator\n')

  while True:
    try:
      cols = int(input('Enter number of columns: '))
      break
    except:
      print('Error: Please enter an integer.')
  while True:
    try:
      rows = int(input('Enter number of rows: '))
      break
    except:
      print('Error: Please enter an integer.')
	
  print('\n')
  print(cols, 'x', rows, 'dot matrix preview:\n')

  dots = [['. ' for j in range(cols)] for i in range(rows)]
  for row in dots:
    print(' '.join([elem for elem in row]))
  print('\n')

  while True:
    type = input('Fill matrix with an (i)nteger or a (c)haracter? ')
    if type in ['i', 'I', 'c', 'C']:
      break
    else:
      print('Please choose i or c.')
      continue
    
  if type == 'i' or type == 'I':
    while True:
      try:
        ivalue = int(input('Choose an integer: '))
        break
      except:
        print('Error: Please enter an integer.')
        continue
    print('\n')
    matrix = [[ivalue for j in range(cols)] for i in range(rows)]
    for row in matrix:
      print('  '.join([str(elem) for elem in row]))
    print('\n')
  elif type == 'c' or type == 'C':
    while True:
      try:
        cvalue = str((input('Choose a character: ')))
        break
      except:
        print('Error: Please enter a character.')
        continue
    print('\n')
    matrix = [[cvalue for j in range(cols)] for i in range(rows)]
    for row in matrix:
      print('  '.join([str(elem) for elem in row]))
    print('\n')

  while True:
    repeat = input('Make a new matrix (y/n)? ')
    if repeat == 'y' or repeat =='Y':
      matrix_generator()
    elif repeat == 'n' or repeat =='N':
      print('Ok, goodbye.')
      break
    else:
      print('Please enter y or n.')
      continue
      
matrix_generator()