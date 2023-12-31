#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 02:21:04 2023

@author: santhoshgunda
"""

def compress_message(msg):
    compressed_msg = ""
    count = 1  # Initialize a count for the current character

    for i in range(1, len(msg)):
        if msg[i] == msg[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed_msg += msg[i - 1] + str(count)
            else:
                compressed_msg += msg[i - 1]
            count = 1  # Reset the count for the new character

    # Handle the last character
    if count > 1:
        compressed_msg += msg[-1] + str(count)
    else:
        compressed_msg += msg[-1]

    return compressed_msg

# Input
msg = input()
compressed_msg = compress_message(msg)

# Output
print(compressed_msg)
