#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profits = prices[1] - prices[0]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profits:
                max_profits = prices[j] - prices[i]
    return max_profits


# print(find_max_profit([50, 10, 2, 50, 90, 100]))
# find_max_profit([1000, 2000, 40, 2])
if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
