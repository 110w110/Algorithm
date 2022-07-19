# import re
#
# a = re.compile("(\D*\(\D*\)\D*|\D*\[\D*\]\D*)*(\.)")
# k = a.match("So when I die (the [first] I will see in (heaven) is a score list).")
# print(k.groups())
# print(a.match("[ first in ] ( first out )."))
# print(a.match(" ."))
# print(a.match("Half Moon tonight (At least it is better than no Moon at all]."))
#
#
# c = re.compile("(((\D)*(\()(\D)*(\))(\D)*)|((\D)*(\[)(\D)*(\])(\D)*))*(\.)")
#
# print(a.split("So when I die (the [first] I will see in (heaven) is a score list)."))
#
#
#
# result = re.match('(\d{2})-(\d{3,4})-(\d{4})', '02-123-1234')
# print(result.groups())
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))