#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


letter_init=''
for letter in range(1,nr_letters+1):
  letter_individual = random.choice(letters)
  letter_init += letter_individual


symbol_init=''
for symbol in range(1,nr_symbols+1):
  symbol_individual = random.choice(symbols)
  symbol_init += symbol_individual


number_init=''
for number in range(1,nr_numbers+1):
  number_individual = random.choice(numbers)
  number_init += number_individual

total_comb = letter_init+symbol_init+number_init
length = len(total_comb)
print(f'Your password is : {total_comb}')

random_string = ''.join(random.sample(total_comb,len(total_comb)))
print(f'Your randomized password is: {random_string}')
