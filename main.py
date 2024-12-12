def main():

    #Testing different string constructs

    stringConstruct1 = 'Its possible to use "Double Quotes" Inside Single Quotes'
    stringConstruct2 = "Its possible to use 'Single Quotes' Inside Double Quotes"
    stringConstruct3a = '''Using three-single quotes is a thing'''
    stringConstruct3b = """Using triple-double quotes is a thing too"""

    print(stringConstruct1)
    print(stringConstruct2)
    print(stringConstruct3a)
    print(stringConstruct3b)
    print("Using quotes in the return to the user is a must and I suppose these string abilities lessens the concern for desired result returnability")

    stringConstruct4 = "if there is only white space between multiple quotated statements", "It combines both statements as if it were one within parenthesis"
    print(stringConstruct4)


if __name__ == "__main__":
    main()
    print("Goodbye!")