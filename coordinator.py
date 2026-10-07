import coordinator
import time 
import subprocess

def run_garmin():
    subprocess.run(["python3","/home/nhi/garmin_other_to_str.py"])

run_garmin()

coordinator.every(24).hours.do(run_garmin)

while True:
    coordinator.run_pending()
    time.sleep(120)