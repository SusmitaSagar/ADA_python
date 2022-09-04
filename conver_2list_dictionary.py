
key_list=['sush','vanshi',4,'nimi']
value_list=['susmita','vanshika','umesh','nimisha']
result = {key_list[i]:value_list[i] for i in range(len(key_list))}
print(str(result))
#{}braces used for dictionary, or for a group
#also used to define a dictionary in a list called literal

#using zip method
result2 = dict(zip(key_list,value_list))
print(str(result2))