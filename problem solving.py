def swap_list(new_list):
    size = len(new_list)

    temp = new_list[0]
    new_list[0] = new_list[size-1]
    new_list[size-1] = temp
    return new_list

list=[1,2,3,4,5]
swap_list(list)
print(list)

def swap2_list(new_list, pos1, pos2):
    size = len(new_list)

    temp = new_list[pos1-1]
    new_list[pos1-1] = new_list[pos2-1]
    new_list[pos2-1] = temp
    return new_list

list=[1,2,3,4,5,6]
swap2_list(list,3,5)
print(list)

def length_list(list):
    count = 0
    for i in list:
        count = count +1

    return count

print(length_list(list))

def max(x,y):
    if x > y:
        return x
    return y
print(max(-2,-6))
a= 500
b=22
maximum = max(a,b)
print(maximum)

def rev_sentence(sen):

    words = sen.split(' ')
    print(words)
    revese_sentence = ' '.join(reversed(words))

    return revese_sentence

input = 'Mustafa Mohamed Adara'
print (rev_sentence(input))

str = "MUstafa A"
count = 0
for i in str:
    count = count +1
print(count)
print(len(str))

def print_even_words(str):
    text = str.split()
    for word in text:
        if len(word)%2 == 0:
            print(word)

def avoid_space(str):
    count = 0
    for i in str:
        if i == " ":
            continue
        else:
            count = count+1
    return count


s =  "geeksforgeeks 33 is   best n m"
print_even_words(s)
print(avoid_space(s))
print(len(s))
