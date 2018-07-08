# Original attempts at parsing
import re
import string

papers = open("The-Federalist-Papers.txt")

lines = papers.read()
papers.close()

elem = re.split(r'FEDERALIST\.? No\.?', lines)
print(len(elem))
for i in range(len(elem)):
    out = open("papers2/" + str(i) + ".txt", "w")
    out.write(elem[i])
    out.close()