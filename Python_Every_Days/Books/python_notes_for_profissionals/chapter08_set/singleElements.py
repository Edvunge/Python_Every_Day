# EXISTENCE CHECK
2 in {1, 2, 3}      #True
4 in {1, 2, 3}      #False
4 not in {1, 2, 3}  #True

# ADD AND REMOVE
s = {1,2,3}
s.add(4)

s.discard(3)
s.discard(5)

s.remove(2)
s.remove(2)


s = {1, 2}
s.update({3, 4})
