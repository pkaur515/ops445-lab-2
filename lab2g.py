#!/usr/bin/env python3

# Author: Prabhjot Kaur
# Author ID: pkaur515
# Date Created: 2025/02/07

import sys
import time

# Check if an argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3  # Default to 3 if no argument is provided

# Countdown loop
while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1

print("blast off!")
