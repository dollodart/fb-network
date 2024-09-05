from secretenv import IN_DIRECTORY, OUT_DIRECTORY, FRIENDS_LIST_HTML, FRIENDS_LIST_TXT

with open(f'{IN_DIRECTORY}/{FRIENDS_LIST_HTML}','r') as _:
    data = _.read()

i = 0
pattern = '"url":"https:\\/\\/www.facebook.com\\/'
ln = len(pattern)

out_file = open(f'{OUT_DIRECTORY}/{FRIENDS_LIST_TXT}', 'w') 

while True:
    i = data.find(pattern)
    if i < 0:
        break
    l = i + ln
    u = data[l:].find('"') + l
    print(l,u,data[l:u])
    print(data[l:u],file=out_file)
    data = data[u:]
