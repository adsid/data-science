secret_number = 9

guess_count = 0

while guess_count < 3 :
    guess_string = input("guess: ")
    guess_count += 1
    if int(guess_string) == secret_number:
        print("You found the secret number")
        break
else:
    print('You lost')

print("Program completed")