

name = 'hello   world  lol'
print(*name.split(" "))
print([s if (len(s) is not 0 and s[0].isdigit()) else s.title() for s in name.split(" ")])
