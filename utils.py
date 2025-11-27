import time

FAST_MODE = True

def slow_print(text):
    global FAST_MODE
    wait = 1
    wait_letter = 0.05
    if FAST_MODE == True:
        wait = 0
        wait_letter = 0

    for word in text:
        print(word, flush= True, end="")
        time.sleep(wait_letter)
    time.sleep(wait)
    print("\n")
