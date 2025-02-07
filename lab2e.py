#!/usr/bin/env python3

import time

# Set the starting number (10)
count = 10

# Timer loop running for countdown
while count > 0:
    print(count)
    time.sleep(1)  # Sleep for 1 second between prints
    count -= 1  # Decrease the count

print("blast off!")

