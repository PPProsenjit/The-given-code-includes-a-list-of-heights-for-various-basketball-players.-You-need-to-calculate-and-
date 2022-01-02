players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = 0
mean = sum(players)/len(players)
add = sum((i-mean)**2 for i in players)

stdvar= (add/len(players))**0.5

low, high = mean-stdvar,mean+stdvar

count = len([v for v in players if low < v < high])
print(count)
