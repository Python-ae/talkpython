# -*- coding: utf-8 -*-
s = "ذهب الطالب الى المدرسة"
with open("file.txt", "w", encoding="utf-8") as myfile:
    myfile.write(s)