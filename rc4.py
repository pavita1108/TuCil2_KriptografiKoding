def scheduling(key):
    schedule = [i for i in range(0,256)]
    key = key [::-1]
    i = 0
    for j in range(0, 256):
        i = (i + schedule[j] + key[j % len(key)]) % 256
        tmp = schedule[j]
        schedule[j] = schedule[i]
        schedule[i] = tmp
        
    return schedule
    

def streamGeneration(schedule):
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (schedule[i] + j) % 256
        
        tmp = schedule[j]
        schedule[j] = schedule[i]
        schedule[i] = tmp
        
        yield schedule[(schedule[i] + schedule[j]) % 256]        


def rc4Encode(text, key):
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]
    
    schedule = scheduling(key)
    key_stream = streamGeneration(schedule)
    
    cipher_text = []
    for char in text:
        enc = (char ^ next(key_stream))
        cipher_text.append(chr(enc))
        
    return (cipher_text)
    

def rc4Decode(ciphertext, key):
    ciphertext = [ord(char) for char in ciphertext]
    key = [ord(char) for char in key]
    
    schedule = scheduling(key)
    key_stream = streamGeneration(schedule)
    
    plaintext = []
    for char in ciphertext:
        dec = char ^ next(key_stream)
        plaintext.append(chr(dec))
    
    return plaintext

# a = 'haisadadada'
# b = 'absddba'
# aa= rc4Encode(a,b)

# print(aa)