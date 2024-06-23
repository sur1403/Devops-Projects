# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

API_TOKEN = 'ATATT3xFfGF0fIEepILQYbGy-TBDfhOdGz4ZVXtgh7gSaaYGzFwtakzgGlm36VmYM-y8wl5umEVLxTCyIOlaX0HzOlAUpS3IlGrkBBEwprtnpX9qL7Un-GXjQcKJ7OXkstmpqkJeYJuk1Ixzk1eMgdb75SM34oMiEsRL0L2-q57-cHAOeyC7QBg=21BA8F45'
EMAIL_ID = 'surbhi.bansal1403@gmail.com'

url = "https://surbhibansal1403.atlassian.net/rest/api/3/issue"


auth = HTTPBasicAuth(EMAIL_ID, API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10005"
    },
    "project": {
      "key": "KAN"
    },
    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
