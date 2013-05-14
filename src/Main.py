# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

#message = 'There can be secret,if two of them are dead.'
message = raw_input('Enter message:')

translated = ''

i = len(message)-1

while i>=0:
    translated = translated + message[i]
    i = i - 1

print(translated)    
    
