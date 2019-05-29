# importing necessary libraries
from itertools import product; from hashlib import md5; from time import time

def bruteforce(pwd) :
    whole_char_set = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;\'",<.>/?' # considers the whole chart
    password_length = 1 # initial password length
    
    while True: # loop through the possible characters of the pwd length
        for char_set in product(whole_char_set, repeat = password_length):
            password = ''.join(char_set)
            h = md5(password.encode('utf-8'))# obtains MD5 of the password
            if h.hexdigest() == pwd: # compares the MD5
                return password
        password_length += 1 # moves on to the next password (by length) to crack
            
hash_filename = 'hashes.txt' # specifying the file to use
with open(hash_filename, 'r') as hf: # opens the file 'hashes.txt'
    for line in hf.readlines(): # processes the file by line
        h = line.strip()
        start_time = time() # reads start time
        password = bruteforce(h)
        end_time = time() # reads end time
        print('{}\t{:6f} seconds'.format(password, end_time - start_time)) # to print results
            


















