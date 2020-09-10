import requests
import json

print("hello")

headers = {
    "Accept": "application/json",
    'Circle-Token': 'cf42538d4913007d488ea6ca02ce01f61f2d4196' 
}

paramters = ""
fetch_api = True
items = []
counter = 0
while fetch_api:
    print("iteration %s" % counter)
    r = requests.get('https://circleci.com/api/v2/project/github/Cazoo-uk/customer-force/pipeline%s' % paramters, headers=headers)
    data = r.json()
    if "next_page_token" in data:
        print(data["items"][-1]["created_at"])
        paramters="?page-token=%s" % data["next_page_token"]
    else:
        fetch_api = False
    if "items" in data:
        items.append(data["items"])
    counter+=1

f = open('test.json', 'w')
f.write(json.dumps(items, indent=2))
f.close()
print("done")