class ArgumentError(Exception):
    pass

def flag(N):
    try:
        N = int(N)
        if N < 1 or N % 2 != 0:
            raise ArgumentError('''Japanese flag couldn't be created using this value''')
    except ValueError:
        raise ArgumentError('''It's not integer''')

    width = N * 3
    height = N * 2
    vertical_distance = N // 2    
    japanese_flag = '#' * (width + 2) + '\n'

    for i in range(height):
        if i in range(vertical_distance) or i in range(height - vertical_distance, height):
            spaces = ' ' * width
            japanese_flag += '#' + spaces + '#' + '\n'
        elif i == N or i == N-1:
            spaces = ' ' * N
            symbol_o = 'o'*(N-2)
            japanese_flag += '#' + spaces + '*' + symbol_o + '*' + spaces + '#' + '\n'
        else:
            if i < N-1:
                spaces_count = height - i - 1      
            else:
                spaces_count = i
            spaces = ' ' * spaces_count
            symbol_o = 'o'*(width - spaces_count*2 - 2)
            japanese_flag += '#' + spaces + '*' + symbol_o + '*' + spaces + '#' + '\n'  

    japanese_flag += '#' * (width + 2)
    return japanese_flag

print(flag(input('Enter number: ')))







