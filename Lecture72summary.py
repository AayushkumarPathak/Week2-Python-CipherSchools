name="aayush"
if name=="aayush":
    print("You are aayush")
elif name=="aayush" or name=="Aayush":
    print("youu are aayush")
else:
    print("You are not aayush")

i=1
while i<10:
    print(i)
    i+=i

for i in range(1,11):
    print(i)
#break keyword
for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)
