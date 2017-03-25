"""
file = open("card_list1.txt")

for line in file:
    line = line.strip()
    line = line + "\""
    newline = line[4:-5] 
    print(newline + " = " + "\"" + line)
    
file.close()
"""

file = open("card_list.py")

all_card_list = []
for line in file:
    line = line.strip()
    line = line 
    print(line)    
    all_card_list.append(line)

print(all_card_list)


file.close()
