import time
def time_function(func, print_output=True):
    start_time = time.time()
    print("Ausgang bei:", func[-1])

    print(f"Dauerte {round((time.time()-start_time)*1000000, 5)} Millisekunden")