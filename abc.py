global file1text,file2text
with open('file1.txt','r') as f1, open('file2.txt','r') as f2:
    file1text = f1.read()
    file2text = f2.read()

open('file1.txt','w').write(file2text)
open('file2.txt','w').write(file1text)

print('file 1: {}, file 2: {}!'.format(file1text,file2text))