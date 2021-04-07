# Dictionaire des valeurs en base 10
sequence = {
    '1':'2048',
    '2': '1024',
    '3': '512',
    '4': '256',
    '5': '128',
    '6': '64',
    '7': '32',
    '8': '16',
    '9': '8',
    '10': '4',
    '11': '2',
    '12': '1',
}

base = '>> '

while True:
    print('Choix de conversion : \n| base 2 en base 10 (1) \n| base 10 en base 2 (2)')
    trad_choice = input(base)

    # Conversion base 2 à base 10
    if trad_choice == '1':
        print('\nConversion base 2 en base 10 \nEx: 0 0 0 0 0 0 0 1 ou 0 0 1 0')
        warning = False
        index = 0
        result_2t10 = 0
        request_2t10 = input(base)
        request_split = request_2t10.split(' ')
        request_length = len(request_split)
        index += len(sequence) - request_length

        for i in request_split:
            index += 1
            if i == '1':
                result_2t10 += int(sequence.get(str(index)))
            elif i == '0':
                result_2t10 = result_2t10
            else:
                print('\nIl n\'y a que des 0 ou de 1 en base 2 !\n')
                warning = True
                break
        if warning == False:
            print(f'\n| {result_2t10} \n')

    # Conversion base 10 à base 2
    elif trad_choice == '2':
        print('\nConversion base 10 en base 2')
        result_10t2 = []
        request_10t2 = int(input(base))

        for i in sequence:
            if request_10t2 >= int(sequence.get(i)):
                request_10t2 -= int(sequence.get(i))
                result_10t2.append('1')
            else:
                result_10t2.append('0')

        print('\n| '+''.join(result_10t2)+'\n')