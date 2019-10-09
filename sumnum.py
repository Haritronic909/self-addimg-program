print('Keep entering the numbers to be added until the final number.\nThen type done to show the sum.')
def main():
    sum = 0.0
    while True:
        great = input ('Enter number: ')
        if great== ('done'):
            break
        elif great==('Done'):
            break
        try:
            sum += float(great)
        except ValueError:
            continue
    print ('The sum is', sum)
main()
