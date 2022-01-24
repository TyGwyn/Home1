#Цифры
d0= 10
d1= 12.5
d2= d0+d1
print(d2)

s0= 'Мама мыла раму.'
s1= 'Папа мыл окно.'
s2= s0 + ' ' + s1
print(s2)

v0 = [0, 1, 2]
v1 = ['0', '1', '2']
v2 = v0 + v1
print(v2)

dct0 = {0:'0', 1:'1'}
keys = ['k'+str(x) for x in range(5)]
values = [x/3.3 for x in range(0, 15, 3)]
dct1 = dict(zip(keys, values))
print(dct1)

for key in dct1.keys():
    print(key, dct1[key])

for key in dct1.keys():
    print('key:{0}, value: {1}'.format(key, int(dct1[key])))

for key in dct1.keys():
    print('key:{}, value: {:.2}'.format(key, dct1[key]))

for key in dct1.keys():
    print(f'key: {key}, value: {dct1[key]}')

for key, value in dct1.items():
    print(f"{key} - {value}")

    a = input(3665)
    # a = '3665'
    a = int(a)

    hours = a // 3600
    scnd = a % 3600
    minutes = scnd // 60
    seconds = scnd % 60

    print(f"{a} секунд это в формате 'чч:мм:сс' - {hours:02}:{minutes:02}:{seconds:02}")
    print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
