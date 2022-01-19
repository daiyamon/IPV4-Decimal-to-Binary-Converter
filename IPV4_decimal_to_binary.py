def binaryConvert(list1):
    answer = []
    final = ""
    list = [128, 64, 32, 16, 8, 4, 2, 1]
    lastNum = len(list1)
    i = 0
    for num in list1:

        for number in list:
            if num >= number:
                num = num - number
                answer.append(1)
            elif num < number:
                answer.append(0)
            elif num == 0:
                answer.append(0)
        i += 1
        if i != lastNum:
            answer.append(".")
    for char in answer:
        final += str(char)



    print(final)
    return final


one = int(input("Enter first number of IPV4 address: "))
two = int(input("Enter second number of IPV4 address: "))
three = int(input("Enter third number of IPV4 address: "))
four = int(input("Enter fourth number of IPV4 address: "))

ipv4 = [one, two, three, four]

binaryConvert(ipv4)