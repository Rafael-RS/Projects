from random import choice
print('Coin flip simulation')
t = h = 0
while True:
    input('Toss the coin!!')
    x = (choice(['tail', 'head']))
    print(x)
    if 't' in x:
        t += 1
    else:
        h += 1
    if input('Do you want to continue(y/n)?') not in 'yY':
        break
print(f'Heads = {h}\nTails = {t}')
