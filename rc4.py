def key_scheduleuling(key):
    scheduleule = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + scheduleule[j] + key[j % len(key)]) % 256
        
        tmp = scheduleule[j]
        scheduleule[j] = scheduleule[i]
        scheduleule[i] = tmp
        
    return scheduleule
    

def stream_generation(schedule):
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
    
    schedule = key_scheduleuling(key)
    key_stream = stream_generation(schedule)
    
    cipher_text = []
    for char in text:
        enc = (char ^ next(key_stream))
        cipher_text.append(chr(enc))
        
    return (cipher_text)
    

def rc4Decode(ciphertext, key):
    ciphertext = [ord(char) for char in ciphertext]
    key = [ord(char) for char in key]
    
    schedule = key_scheduleuling(key)
    key_stream = stream_generation(schedule)
    
    plaintext = []
    for char in ciphertext:
        dec = char ^ next(key_stream)
        plaintext.append(chr(dec))
    
    return plaintext
