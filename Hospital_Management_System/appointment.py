import datetime
import random
def appoint():
    print(f"Appointment Date : \n {datetime.datetime.now()}")
    print(f"Generated Token Number : \n{random.randint(1000,9999)}")