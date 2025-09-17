take =input("Enter the char \n'M' for monday\n'T' for tuesday \n'W' for Wednesday\n'Th' for Thursday \n'F' for Friday \n'S' for Saturday\n'Sn' for Sunday\n ")
print()
match take :
    case 'M':
        print('Monday')
    case 'T':
        print('Tuesday')
    case 'W':
        print('Wednesday')
    case 'Th':
        print('Thursady')
    case 'F':
        print('Friday')
    case 'S':
        print('Saturday')
    case 'Sn':
        print('Sunday')
    case _:print("Invalid ")