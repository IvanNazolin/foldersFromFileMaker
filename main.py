import codecs
import os

i=1
with codecs.open('file.txt', encoding='utf-8') as fin:
    while True:
        line = fin.readline()
        print(line)
        if not line:
            break
        os.mkdir(f"{str(i)+'.'+line[:-2]}")
        i+=1
fin.close()