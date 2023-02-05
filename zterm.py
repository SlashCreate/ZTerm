import subprocess
import platform
import time
import os
import numpy as np

class txt:
    red = "\u001b[0;31m"
    green = "\u001b[0;32m"
    yellow = "\u001b[0;33m"
    blue = "\u001b[0;34m"
    magenta = "\u001b[0;35m"
    cyan = "\u001b[0;36m"
    white = "\u001b[0;37m"
    underline = "\u001b[4m"
    bold = "\u001b[1m"
    inverse = "\u001b[7m"
    end = "\u001b[0m"

fname = "files/userinfo/user.i"
f = open(fname)
lines = f.read().splitlines()
f.close()

path = '/files'
user = txt.green + lines[0] + '@' + lines[1] + txt.end + ' > '
os.system('clear')

print(txt.cyan + txt.bold + 'Zterm' + txt.white + txt.underline + ' 1.00\n')
while True:
  code = input(user)
  args = code.split('`')
  cmd = args[0]

  if cmd == '--clr':
    os.system('clear')
  elif cmd == '--folder':
    path = args[1]
    dir_list = os.listdir(path)
    print("Files in ", path, ":")
    for i in dir_list:
      print(i)
  elif cmd == '--runpy':
    exec(open(args[1]).read())
  elif cmd == '--help':
    if len(args) == 1:
      print(' --runpy`<file>       Runs python3 file')
      print(' --str`<txt>`<c>      Prints <txt>. Use <c> for styling (optinal)')
      print(' --clr                Clears screen')
      print(' --folder             Lists all files and folders')
      print(' --help`<cmd>         Opens help screen')
    if len(args) == 2:
      if args[1] == '--str':
        print('Colors: (optinal, for <c>)')
        print('white' + '   value = 0')
        print(txt.end + txt.red + 'red' + txt.end + '   value = 1')
        print(txt.end + txt.green + 'green' + txt.end + '   value = 2')
        print(txt.end + txt.yellow + 'yellow' + txt.end + '   value = 3')
        print(txt.end + txt.blue + 'blue' + txt.end + '   value = 4')
        print(txt.end + txt.magenta + 'magenta' + txt.end + '   value = 5')
        print(txt.end + txt.cyan + 'cyan' + txt.end + '   value = 6')
        print(txt.end + txt.underline + 'underline' + txt.end + '   value = 7')
        print(txt.end + txt.bold + 'bold' + txt.end + '   value = 8')
        print(txt.end + txt.inverse + 'inverse' + txt.end + '   value = 9')
          
        print('\nSyntax: ')
        print('--str`<text>`<c>')
        
      if args[1] == '--folder':
        print('Syntax: ')
        print('--folder`<folder>')
        
      if args[1] == '--clr':
        print('Syntax: ')
        print('--clr')

      if args[1] == '--runpy':
        print('Syntax: ')
        print('--runpy`<file>')
  elif cmd == '--str':
    if len(args) == 2:
      print(txt.end + args[1])
    elif len(args) == 3:
      if int(args[2]) == 0:
        print(txt.end + args[1])
      if int(args[2]) == 1:
        print(txt.end + txt.red + args[1] + txt.end)
      if int(args[2]) == 2:
        print(txt.end + txt.green + args[1] + txt.end)
      if int(args[2]) == 3:
        print(txt.end + txt.yellow + args[1] + txt.end)
      if int(args[2]) == 4:
        print(txt.end + txt.blue + args[1] + txt.end)
      if int(args[2]) == 5:
        print(txt.end + txt.magenta + args[1] + txt.end)
      if int(args[2]) == 6:
        print(txt.end + txt.cyan + args[1] + txt.end)
      if int(args[2]) == 7:
        print(txt.end + txt.underline + args[1] + txt.end)
      if int(args[2]) == 8:
        print(txt.end + txt.bold + args[1] + txt.end)
      if int(args[2]) == 9:
        print(txt.end + txt.inverse + args[1] + txt.end)
    else:
      print(txt.red + 'Could not find argument(s)' + txt.end)
  elif cmd.startswith('') == True:
    pass
  else:
      print(txt.white + 'Could not find command ' + txt.end + cmd)
  
