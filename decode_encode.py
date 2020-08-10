x = b'\xd9\x87\xd9\x84\xd8\xa7'

x = "ذهب الطالب الى المدرسة"

eee = x.encode('utf-8')

print('endcoded: ', eee)

ddd = eee.decode('utf-8')

print(ddd)
