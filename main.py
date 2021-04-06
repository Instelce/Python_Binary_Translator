# Dictionaire des valeurs en base 10
base_2 = {
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

while True:
    index = 0
    result = 0
    request_bin = input(' > ')
    request_split = request_bin.split('.')
    request_length = len(request_split)
    index += len(base_2) - request_length

    for i in request_split:
        index += 1
        if i == '1':
            result += int(base_2.get(str(index)))
    print(f'\n| {result} \n')
