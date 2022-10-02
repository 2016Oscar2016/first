import requests

res_parse_list = []
response = requests.get("https://finance.ua/ua/currency")
response_text = response.text

print(response_text)
response_parse = response_text.split("<span>")

for parse_1 in response_parse:
    if parse_1.startswith("class=c2>"):
        for parse_2 in parse_1.split("</span>"):
            if parse_2.startswith("class=c3>") and parse_2[1].isdigit():
                res_parse_list.append(parse_2)

dollar_change_rate = res_parse_list[0]
print(f"Dollar: {dollar_change_rate}")
euro_change_rate = res_parse_list[1]
print(f"Euro: {euro_change_rate}")