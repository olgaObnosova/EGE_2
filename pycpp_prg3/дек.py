import collections
d = collections.deque()
d.append(1)
print(d)
d.append(2)
d.appendleft(0)
print(*d)
d.pop()
print(*d)
d.popleft()
print(*d)
