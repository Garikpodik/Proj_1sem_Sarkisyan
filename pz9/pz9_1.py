a = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
g = [] 
m = [] 
eda = {}
b = a.split()

for i in b[1:6]:
    g.append(int(i))
eda[str(b[0])] = g

for i in b[7:12]:
    m.append(int(i))
eda[str(b[6])] = m
print(eda)

print('максимальные продажи апельсинов:', max(g))
print('максимальные продажи яблок:', max(m))