print('Keep entering the numbers to be added until the final number.\nThen type done to show the sum.')
def main():
    sum = 0.0
    while True:
        calc = input ('Enter number: ')
        if calc== ('done'):
            break
        elif calc==('Done'):
            break
        try:
            sum += float(calc)
        except ValueError:
            continue
    print ('The sum is', sum)
main()
