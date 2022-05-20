import json

info = open('movies3.json', 'rt', encoding='UTF8')
res = json.load(info)
titles = []
for r in res:
   titles.append(r['fields']['title'])
titles = "','".join(titles)
f = open('title.txt', 'w', encoding='UTF8')
f.write(titles)
# for title in titles:
#     f.write(title+',')
f.close()