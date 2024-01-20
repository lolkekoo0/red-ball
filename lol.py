a = []
sum = 0
while True:
    b = int(input())
    if b ==0:
        break
    print(a.append(b))
    print(a)
for i in range(4):
    sum=sum+a[i]

print("средний возраст всех людей",sum/4, "лет")

