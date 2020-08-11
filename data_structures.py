#Data structures playground
#1. Dictionaries
# 2. Lists / arrays [1,2,3,22]
# 3. Sets


lst = [1, 1, 11, 7]
print(lst)
lst.append(15)
print(lst)
lst.remove(11)
lst.sort()
print(lst)


# Sets:
st = {1, 1, 11, 7}
st.add(1)
st.add(1)
st.add(11)
print(st)


# Dictionaries

d = {
    'bob': 0,
    'sarah': 0,
    'defeated_by': {'paper', 'wolf'},
    'defeats': {'sponge', 'scissors'}
}
print(d)
d['bob']
