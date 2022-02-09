'''
Proyecto #64 del libro The big book of small python projects
'''

'''
Módulo display de 7 segmentos tipo:

 _A_
|   |
F   B
|_G_|
|   |
E   C
|_D_|

'''


def getSevStr(number, minWidth=0):

    # Completa con 0 a la izq
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Hace que no se mande el espacio entre char de más abajo

        elif numeral == '-':
            rows[0] += ' '
            rows[1] += '_'
            rows[2] += ' '

        elif numeral == '0':
            rows[0] += ' _ '
            rows[1] += '| |'
            rows[2] += '|_|'
        elif numeral == '1':
            rows[0] += '   '
            rows[1] += '  |'
            rows[2] += '  |'

        elif numeral == '2':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += '|_ '

        elif numeral == '3':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += ' _|'

        elif numeral == '4':
            rows[0] += '   '
            rows[1] += '|_|'
            rows[2] += '  |'

        elif numeral == '5':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += ' _|'

        elif numeral == '6':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += '|_|'

        elif numeral == '7':
            rows[0] += ' _ '
            rows[1] += '  |'
            rows[2] += '  |'

        elif numeral == '8':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += '|_|'

        elif numeral == '9':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += '  |'

        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


if __name__ == '__main__':
    number = '123.456.789.0'
    print(getSevStr(number))
