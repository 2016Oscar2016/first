import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")

for parse_1 in response_parse:
    if parse_1.startswith("$"):
        for parse_2 in parse_1.split("</span>"):
            if parse_2.startswith("$") and parse_2[1].isdigit():
                res_parse_list.append(parse_2)
bitcoin_change_rate = res_parse_list[0]
print(f"Bitcoin: {bitcoin_change_rate}")
ethereum_change_rate = res_parse_list[1]
print(f"Ethereum: {ethereum_change_rate}")
