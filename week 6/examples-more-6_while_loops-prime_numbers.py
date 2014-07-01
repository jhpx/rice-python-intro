# While Loops
# Prime Numbers


# This program prints a list of the prime numbers from 0 to
#	an input number using a method called the Sieve of 
#	Eratosthenes.

import simplegui
import math

# Global Variables

width = 100
height = 100
        
# Event Handlers

def get_primes(text):
    if text.isdigit() and int(text) > 0:
        if int(text) == 1:
            print "There are no prime numbers in range."
        else:
            nums = range(2, int(text) + 1)
            ans = []
            # The loop continues until all composite numbers
            #	have been removed from nums and all prime
            #	numbers have been transferred to ans.
            while len(nums) > 0:
                x = nums[0]
                ans.append(nums[0])
                for n in list(nums):
                    if n % x == 0:
                        nums.remove(n)
            print "Prime numbers in range:", ans
    else:
        print "Please enter a counting number greater than 1."
    
# Frame

frame = simplegui.create_frame("Prime Numbers", width, height)
frame.add_input("Enter a counting number:", get_primes, 100)

# Start

frame.start()