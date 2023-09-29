from inspect import signature


def sort_file(*csv_string, insep=',', intend='\n', outsep='in', outend='in'):
    if len(csv_string) > 1:
        print(len(csv_string))
        raise TypeError("Only one positional argument is allowed")

    print("Original string is: " + repr(csv_string))

    #sort incoming csv string
    # sorted_csv_string = intend.join(sorted(csv_string.split(intend)))
    # print("Sorted string is: " + str(sorted_csv_string))

    #sorted string to list and remove unnecessary elements
    csv_list = str(csv_string[0]).splitlines()
    for el in csv_list:
        if '#' in el:
            csv_list.remove(el)

    while True:
        try:
            csv_list.remove("")
        except ValueError:
            break
    print("Result list:" + str(csv_list))

    #sort list
    csv_list.sort()

    #list to new csv string
    result_string = ""
    pos = -1
    for el in csv_list:
        pos += 1
        if pos == len(csv_list) - 1:  #last element in list
            result_string += el
        else:
            result_string += el + intend
    print("New string is: " + repr(result_string))

    #replacing elements
    if (outsep != 'in'):
        result_string = result_string.replace(',',outsep)

    if (outend != 'in'):
        result_string = result_string.replace('\n',outend)

    print("Final string is: " + repr(result_string))

    return result_string


# test_string = "#b,b\ny,y\na,a"
#sort_file('b,b\ny,y\na,a', outsep=':')
#sort_file('b,q\n\n#p,y\na,o', outsep='-')   #'a-o\nb-q'

#sort_file('abc', 'test')
#sort_file('abc')
#sort_file('2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a')
#sort_file('4,1,d')
# print(signature(sort_file).parameters['args'].kind)