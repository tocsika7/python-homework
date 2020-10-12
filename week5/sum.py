def main():
    ''' 1-100-ig a számok számjegyeinek összege. 
    Minden számot hozzáfűz egy stringhez majd ezeket int-re konvertálva
    helyezzük be egy listába és szummázzuk az értékeket.  
    '''
    digits = ''
    for i in range(1,100+1):
        digits += str(i)

    li = [int(d) for d in list(digits)]
    print(sum(li))
   
if __name__ == "__main__":
    main()