#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: Sep 2019
# This program adds integers


def main():
    # this function calculates the total

    # input
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))

    # process
    total = number_one + number_two

    # output
    print("")
    print("The total is: {}"
          .format(total))


if __name__ == "__main__":
    main()
