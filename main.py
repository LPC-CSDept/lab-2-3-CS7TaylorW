def main():
    ##################################################
    # Comlete your code here
    ##################################################

    var1 = int(input("Please enter your first number."))
    var2 = int(input("Please enter your second number."))
    var3 = int(input("Please enter your third number."))
    sum = (var1 + var2 + var3)
    avg = (sum / 3)
    print ('Values:', var1, var2, var3)
    print ('Total:', sum)
    print (f'Average: {avg:.2f}')

    pass


if __name__ == '__main__':
    main()
