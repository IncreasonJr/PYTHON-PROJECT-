secret_number=4
attempts=3
guess=int(input('Guess the correct number: '))
if guess==secret_number:
    print('Correct answer')
else:
    while attempts>1:
        attempts-=1
        print(f'Incorrect answer. You have {attempts} attempts left')
        guess=int(input('Guess the correct number: '))
        if guess==secret_number:
         print('Correct answer')
         break
    else:
        print('You are out of attempts')
