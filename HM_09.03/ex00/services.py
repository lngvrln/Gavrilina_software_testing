# services.py 
import time
import random

def service_unique_id(): 
    unique_id = int(time.time() * 1000) + random.randint(0, 999)
    return unique_id 

