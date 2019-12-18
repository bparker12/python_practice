import random

my_randoms = list()

for i in range(10):
    my_randoms.append(random.randrange(1, 9, 1))


"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

numbers_1_to_10 = range(1, 10)

for number in numbers_1_to_10:
    if number in my_randoms:
        count = my_randoms.count(number)
        sentence = f'{number} is in the random list {count} time'
        if count == 1:
            print(sentence)
        else:
            print(sentence  + 's')
            
    else:
        print(f'{number} is not in the random list')


    