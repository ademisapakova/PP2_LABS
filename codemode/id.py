d = {
    'Zhapar': '20B8712398123',
    'Vcxvb': '19B8712398123',
    'Zhapazxcvzxvr': '20B8712398123',
    'Ernat': '18B8712398123'
}

dy = list(sorted(d,key = lambda x: (x[1][:3], x[0][1])))

for k,v in dy:

    print(k,v)
