# encrypting a character
def encrypt_char(char,key):
  return chr(ord('A') + (ord(char) - ord('A') + key ) % 26)

#encrypt the message
def encrypt_message(message,key):
  cipher = ''
  message = message.upper()
  for c in message:
    if c in '. ,_-()!@#$%^&*1234567890':
      cipher = cipher + c
    else:
      cipher = cipher + encrypt_char(c,key)
  return cipher

#output
message = input("Enter a message: ")
key = int(input("Enter a key:"))
print("Encrypted message is: ",encrypt_message(message,key))


#decrypting character
def decrypt_char(char,key):
  return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)

#decrypt the message by reversing the algorithm
def decrypt_message(cipher,key):
  message = ''
  for c in cipher:
    if c in '. ,_-()!@#$%^&*1234567890':
      message = message + c
    else:
      message = message + decrypt_char(c,key)
  return message

#decrypting the message by using same algorithm
def decrypt_message2(cipher,key):
  return encrypt_message(cipher,26-key)

print(decrypt_message2('PB QDPH LV UDMXO',3)) #example
