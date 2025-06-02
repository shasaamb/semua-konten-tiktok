import time
import string

target = "kamu ganteng banget hari ini"
letters = string.ascii_lowercase + " .,!?ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
current_str = ""

while current_str != target:
    for letter in letters:
        print(current_str + letter)
        time.sleep(0.02)
        if current_str + letter == target[:len(current_str) + 1]:
            current_str += letter
            break
