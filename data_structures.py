#Data structures playground
#1. Dictionaries
# 2. Lists / arrays [1,2,3,22]
# 3. Sets

# lists
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
# d = dict()
# d = {}
# d = dict(bill=2, zoe=7, michael=4)
# d = {'bill': 2, 'zoe': 7, 'michael': 4}

d = {
    'bob': 0,
    'sarah': 0,
    'defeated_by': {'paper', 'wolf'},
    'defeats': {'sponge', 'scissors'}
}

print(d['bob'])
d['bob'] +=1
print(d['bob'])
print(d)
d['michael'] = 7
print(d)
print(f"You are defeated by {d['defeated_by']}")
print(d.get('other', 42))
