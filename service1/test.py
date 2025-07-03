import os
import time
from datetime import datetime
print("this is service1")

log_dir = os.path.join(os.path.dirname(__file__), 'logs')

os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "service1.log")

while True:
    with open(log_file, "a") as file:
        msg = f"Service 1 : {datetime.now()}"
        file.write(msg)
        print(msg)
    time.sleep(1)

