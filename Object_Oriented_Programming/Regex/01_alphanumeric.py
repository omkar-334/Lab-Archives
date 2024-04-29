import re
string='HelloOmka   '
pattern1=r'^[a-zA-Z0-9]+$'
out1=re.search(pattern1,string)
print(bool(out1))