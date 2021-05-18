import subprocess

# getting the wifi divice name

r = subprocess.check_output(['netsh','wlan','show','Network', 'mode=BSSID']).decode("utf-8")
ls = r.split("\n")
##for ii in ls:
##    print(ii)

name = []
strength = []
count = 0
popInd = []
# collections of name and strenght in list
for lst in ls:
    temp = []
    if 'SSID' in lst and 'BSSID' not in lst:
        name.append(lst.split(':')[1].replace('\r','').replace(' ',''))
    if 'Signal' in lst:
        test = lst.split(',')[0].split(':')
        if 'BSSID' not in test[0]:
            name.append(test[1].replace('%','').replace('\r','').replace(' ',''))

#separating the name and strenght
while count < len(name):
    ind = []
    count+=1
	
    while count < len(name) and name[count].isnumeric():
        ind.append(int(name[count]))
        popInd.append(count)
        count+=1
    strength.append(ind)

for ii in popInd[::-1]:
    name.pop(ii)

for i,j in zip(name,strength):
    print(i,j)
