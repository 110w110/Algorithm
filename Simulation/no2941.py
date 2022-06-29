import re
t = input()
c = re.compile('c\=|c\-|dz\=|d\-|lj|nj|s\=|z\=')
print(len(re.sub(c,'x',t)))