alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #search new position only for char from alphabet, ignore any others ex:3_
    if char in alphabet:    
      position = alphabet.index(char)
      new_position = position + shift_amount
      #by decode doesn't matter cause lists in python intrepret negative numbers to go reverse 
      if new_position > 26: 
        new_position = new_position - 26
      end_text += alphabet[new_position]
    else: 
      end_text += char    
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

import art
print(art.logo)

end_game = False 

while end_game == False: 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #check if user enter more then 26 get the rest of the number
  if shift > 26:
    shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("do you want to restart? (y/n)\n").lower()
  if "n" in restart: 
    end_game = True