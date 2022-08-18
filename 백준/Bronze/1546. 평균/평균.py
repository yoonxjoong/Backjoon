cnt = input()
data = list(map(int, input().split()))
max_value = max(data)
#print("max_value : " + max_value)
#print(data)
for i in range(len(data)):
  #if data[i] != max_value:   
    data[i] = data[i] / max_value * 100
    #print(data[i])
#print(data)
result = sum(data)
print(result / len(data))