import random

user_name=input('Enter your name: ')
user_age=int(input('Enter your age: '))
user_birth_place=input('Enter your birth place: ')

user_data=[user_name,user_age,user_birth_place]

pick_name=user_data[0]
pick_age=user_data[1]
pick_birth_place=user_data[2]


sentence_one_group=[
    f'My name is {pick_name}',
    f'{pick_name} is my name',
    f'I am {pick_name}',
    f'Regarding me, my name is {pick_name}'
]

sentence_two_group=[
    f'I mean, I\'m {pick_age}',
    f'I am {pick_age} years of age',
    f'I\'m {pick_age} right now',
    f'I have {pick_age} years'

]

sentence_three_group=[
    f'I live at {pick_birth_place}',
    f'My home is {pick_birth_place}',
    f'I\'m based in {pick_birth_place}',
    f'I\'m a resident of {pick_birth_place}'
]

sentence_one=random.choice(sentence_one_group)
sentence_two=random.choice(sentence_two_group)
sentence_three=random.choice(sentence_three_group)

paragraph=f'{sentence_one}. {sentence_two}. {sentence_three}'

print(paragraph)
