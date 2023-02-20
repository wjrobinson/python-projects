alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
       break
    else:
       continue  

text = input("Type your message:\n").lower()

while True:
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
       print("Please enter an integer value.")
       continue
    else:
       break  

def caesar(plain_text, shift_amount, direction_value):
  end_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction == "encode":
        new_position = position + shift_amount
    elif direction == "decode":
        new_position = position - shift_amount
    end_text += alphabet[new_position]
  print(f"The {direction}d text is {end_text}.")

caesar(plain_text=text, shift_amount=shift, direction_value=direction)
