s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
s = s.replace(",","")
s = s.replace(".","")
list = s.split(" ")
ss = set(list)
ss = sorted(ss)
for x in ss:
    print(x)
print()
for x in ss:
    y = s.count(x)
    print(x," : ",y)
