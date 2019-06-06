#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    result = []
    options = ["rock", "paper", "scissors"]

    def inner_function(rounds, temp_array=[]):
      # If base case, append the temp_array that has been accumulating possible options
        if rounds == 0:
            result.append(temp_array)
            return
        else:
          # recursive case, calls its self decrementing the number of rounds and adding next option to the temp array
            for option in options:
                inner_function(rounds - 1, temp_array + [option])

    # calls recursive function
    inner_function(n)
    return result


# print(rock_paper_scissors(2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
