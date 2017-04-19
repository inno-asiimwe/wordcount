def words(string):
    #splitting the string into a list
    word_list = string.split()

    #checking for any digits in the list items
    for i in range(0,len(word_list)):
        if word_list[i].isdigit():
            word_list[i] = int(word_list[i])

    #creating a dictionary from the list of words to be returned by the function
    dic = {item:word_list.count(item) for item in word_list}
    return dic
