##Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and 
#validates it to make sure that it is a valid number (look into how credit cards use a checksum).

def inpt():
    while True:
        x = input("CARD NUMBER: ")
        if x.replace("-",'').isnumeric():
            if len(x) == 16:
                x = int(x.replace('-',''))
                break

            else:
                print("ENTER 16 digit value")
        else:
            print("NOT a Valid input")
    return x

def luhn_algo():
    num = inpt()
    def strtoint(n):
        return [int(n) for n in str(n)]
    num = strtoint(num)
    odd_num = num[-1::-2]
    even_num = num[-2::-2]

    checksum = 0
    checksum += sum(odd_num)

    for x in even_num:

        checksum += sum(strtoint(x*2))

    if checksum % 10 == 0:
        print("VALID")
    else:
        print("INVALID")

if __name__ == '__main__':
    luhn_algo()