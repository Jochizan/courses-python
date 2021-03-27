cas = int(input())
for t in range(1, cas+1):
    n = int(input())

    d = {}
    for i in range(n):
        person = input()
        d[person] = len(set(person.replace(" ","")))
        
    for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        print("Case #{}: {}".format(t, key))
        break