print('Keep entering the numbers to be added until the final number.\nThen type done to show the sum.')
def main():
    sum = 0.0
    while True:
        calcu = input ('Enter number: ')
        if calcu== ('done'):
            break
        elif calcu==('Done'):
            break
        try:
            sum += float(calcu)
        except ValueError:
            continue
    print ('The sum is', sum)
main()
