fhan=open("regex_sum_102136.txt")
import re
print(sum([float(x) for x in (re.findall("[0-9]+",fhan.read()))]))
