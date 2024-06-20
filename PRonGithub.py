# emply tuple 
# empty_tuple = ()
# empty_list = []
# empty_dict = {}
# empty_set = set()

    
import requests

url = f"https://api.github.com/repos/hashicorp/terraform/pulls"

response = requests.get(url)

if response.status_code == 200:
    pull_requests = response.json()

    pr_creators = {}

    for pr in pull_requests:
        creator = pr['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    for user, count in pr_creators.items():
        print(f"{user} has created {count} PRs")
    
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
     



    




