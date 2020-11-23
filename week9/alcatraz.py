import math

CELL_NUM = 600

def isPerfectSquare(num):
    root = math.sqrt(num)
    return int(root + 0.5) ** 2 == num     

def main():
    open_cells = []
    for cell in range(1,CELL_NUM + 1):
        if isPerfectSquare(cell):
            open_cells.append(cell)
    
    print(open_cells)

    

if __name__ == "__main__":
    main()