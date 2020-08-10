import codecs

file1 = codecs.open('text.txt','r','utf8')
content = file1.read()
encoded = content.encode('utf-8')
print(encoded)

words = content.split()
print(words)
# for x in words:
#     print (x)
file1.close()
