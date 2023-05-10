seq1 = 'atbasdsqwepincvarsdlzqolsebn'
seq2 = 'atbasdsqwepincvarsdlzqolssbn'
zip_seqs= zip(seq1,seq2)
enum_seq= enumerate(zip_seqs)
# print(list(enum_seq))

for i ,(a,b) in enum_seq:
    if a!=b:
        print(f' index: {i} {a,b}')

fruits = {'apple': 25, 'banana': 14, 'mango':48, 'cherry': 30}
fruits2= enumerate(fruits)
for x in enumerate(fruits2):
    print(x)