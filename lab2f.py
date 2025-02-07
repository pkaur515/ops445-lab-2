#!/usr/bin/env python3

# Author: Prabhjot KAur
# Author ID: pkaur515
# Date Created: 2025/02/07

import sys
import time

# Get the value from command-line argument
timer = int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1

print("blast off!")

