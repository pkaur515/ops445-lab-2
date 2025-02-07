#!/usr/bin/env python3
import sys

# Check if there are enough arguments
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit(0)  # Exit with a success code (0)

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + age + " years old.")

