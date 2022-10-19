#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import copy
import itertools


def get_maximums(numbers):
	return [max(i) for i in numbers]

def join_integers(numbers):
	return "".join([str(i) for i in numbers])

def generate_prime_numbers(limit):
	primes = []
	numbers = [n for n in range(2, limit + 1)]
	while numbers!=[]:
		primes.append(numbers[0])
		for p in primes:
			numbers = [n for n in numbers if n%p != 0]
	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	if excluded_multiples == None: return [e+str(n) for n in range(1,num_combinations+1) for e in strings ]
	else: return [e+str(n) for n in range(1,num_combinations+1) if n % excluded_multiples != 0 for e in strings ]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(37))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
