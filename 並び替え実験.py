#listの並び替え
num_list = [50,30,10,20,40]
num_list_1 = ["a","b","c","d","e"]
cut = zip(num_list,num_list_1)
cuts = sorted(cut)
num_list,num_list_1 = zip(*cuts)
print(num_list)
print(num_list_1)
