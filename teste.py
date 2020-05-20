frutas = [
    {'fruta':'maca', 'quantidade': 10},
    {'fruta':'laranja', 'quantidade': 20},
    {'fruta':'maca', 'quantidade': 40},
    {'fruta':'uva', 'quantidade': 50},
    {'fruta':'laranja', 'quantidade': 10}]

a = {}

for x in frutas:
    if x['fruta'] not in a:
        a[x['fruta']] = x['quantidade']
        print(a)
    else:
        a[x['fruta']] += x['quantidade']

print(a)