#!/usr/bin/python3
for i in range(100):
    formatted_number = f"{i:02}"
    print(formatted_number, end=", " if i < 99 else "\n")
