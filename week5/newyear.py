def main():
    ''' Kétezerhúsz kiíratása számjegyek használata nélkül. 
    Egy string karaktereinek az ascii értékének összege adja a számot. 
    '''
    print(sum(ord(c) for c in 'alma alma alma alma al+'))

if __name__ == "__main__":
    main()