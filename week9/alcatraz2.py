CELL_NUM = 600

def main():
    cells = [False for c in range(1,CELL_NUM + 1)]
    open_cells = []
    for turn in range(1, CELL_NUM + 1):
        for cell_index, cell in enumerate(cells, start=0):
            if cell_index % turn == 0:
                cells[cell_index] = not cells[cell_index] 

    for cell_index, cell in enumerate(cells, start=0):
        if cell:
            open_cells.append(cell_index)
    
    for cell in open_cells:
        print(cell, end='')


if __name__ == "__main__":
    main()