# Python: 'list' object attribute 'append' is read-only

a_list = ['bobby', 'hadz', '.']

# ✅ Correctly using list.append()
a_list.append('com')

a_list.append('xyz')

# ['bobby', 'hadz', '.', 'com', 'xyz']
print(a_list)