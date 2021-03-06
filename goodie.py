import sys

f = open('input.txt', 'r')
lines = f.readlines()

while '\n' in lines:
  lines.remove('\n')

n = int(lines[0].split(':')[1])

ln = len(lines)

del lines[0]
del lines[0]

for x in range(0,ln-3):
  lines[x] = lines[x][:-1]

item_price = []

item = []
price = []

lent = len(item_price)

for x in lines:
    split_str = x.split(':')
    item.append(split_str[0])
    price.append(int(split_str[1].strip()))
    item_price.append([int(split_str[1].strip()),split_str[0]])

item_price.sort()

least_diff = sys.maxsize  
lent = len(item_price)

si = 0
ei = 0

for x in item_price:
  print(x)

for x in range(0, lent-n+1):
  diff = item_price[x+n-1][0] - item_price[x][0]
  print(diff, item_price[x+n-1][0], item_price[x][0])
  if diff<least_diff:
    least_diff = diff
    si = x
    ei = x+n
  
for x in range(si, ei):
  print(item_price[x])

f = open('output.txt', 'w')

f.write("The goodies selected for distribution are:\n\n")

for x in range(si, ei):
  f.write(str(item_price[x][1]) + ": " + str(item_price[x][0]) + "\n")

f.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(least_diff))