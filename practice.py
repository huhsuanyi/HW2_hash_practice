f = open('/hw2_data.txt')
text=[]
for line in f:
     text.append(line)
len(text)
892

dict={}
for i in range(0,891):
    if text[i] not in dict:
        dict[text[i]]=1

    if text[i] in dict:
        dict[text[i]]+=1
dict
{'Cheese\n': 235,
 'Pizza\n': 84,
 'Coke\n': 145,
 'Steak\n': 47,
 'Burger\n': 197,
 'Fries\n': 77,
 'Rib\n': 34,
 'Taco\n': 58,
 'Pho\n': 20,
 'Potato\n': 4}
