

def wc(text):
    wc = 0
    for i in text:
        wc += 1
    return wc

    
def char(text):
    dictionary = {}
    for letter in text.lower():
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    return dictionary
    
def sort_on(dict):
    return dict["num"]

def sorted(char):
    sorted_dic = []
    for key in char:
        value = char[key]
        sorted_dic.append({"char":key,"num":value})
    sorted_dic.sort(reverse=True, key=sort_on)
    return sorted_dic


