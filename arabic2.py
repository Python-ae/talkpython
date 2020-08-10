# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

text = "ذهب الطالب الى المدرسة"
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction

print(u"ذهب الطالب الى المدرسة")
print(reshaped_text)
print(bidi_text)