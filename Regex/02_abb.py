import re
string='abcc'
pattern1=r'ab*'
out1=re.search(pattern1,string)
print(bool(out1))