SUM = 90
PROD = 996300

from itertools import combinations
from numpy import prod


def main():
    possibleNums = [n for n in range(1,45+1) if PROD % n == 0]
    for comb in combinations(possibleNums, 6):
        if sum(comb) == SUM and prod(comb) == PROD:
            print(comb)

    
if __name__ == "__main__":
    main()