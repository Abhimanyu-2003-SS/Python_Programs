import patient
import doctor as doc
from billing import bill
import appointment
import pandas
import sys
import importlib
patient.patient_details()
doc.docter_details()
appointment.appoint()
bill()
if "__name__"=="__main__":
    print("Current Module Name : \n __main__")
print("Imported Modules:")
print(sys.modules.keys())
print(sys.path)
importlib.reload(patient)

print("Module Reloded Successfully")

print("Thank You For Using Hospital Management System")