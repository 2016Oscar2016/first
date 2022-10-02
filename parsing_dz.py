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
        for parse_3 in parse_2.split("</span>"):
            if parse_3.startswith("$") and parse_3[2].isdigit():
                res_parse_list.append(parse_3)
        for parse_3 in parse_2.split("</span>"):
            if parse_3.startswith("$") and parse_3[2].isdigit():
                res_parse_list.append(parse_3)
        for parse_4 in parse_3.split("</span>"):
            if parse_4.startswith("$") and parse_4[3].isdigit():
                res_parse_list.append(parse_4)
        for parse_5 in parse_4.split("</span>"):
            if parse_5.startswith("$") and parse_5[4].isdigit():
                res_parse_list.append(parse_5)
        for parse_6 in parse_5.split("</span>"):
            if parse_6.startswith("$") and parse_6[5].isdigit():
                res_parse_list.append(parse_6)
        for parse_7 in parse_6.split("</span>"):
            if parse_7.startswith("$") and parse_7[6].isdigit():
                res_parse_list.append(parse_7)
        for parse_8 in parse_7.split("</span>"):
            if parse_8.startswith("$") and parse_8[7].isdigit():
                res_parse_list.append(parse_8)
        for parse_9 in parse_8.split("</span>"):
            if parse_9.startswith("$") and parse_9[8].isdigit():
                res_parse_list.append(parse_9)
        for parse_10 in parse_9.split("</span>"):
            if parse_10.startswith("$") and parse_10[9].isdigit():
                res_parse_list.append(parse_10)

print("Top 10 by popularity")
bitcoin_change_rate = res_parse_list[0]
print(f"1. Bitcoin: {bitcoin_change_rate}")

ethereum_change_rate = res_parse_list[1]
print(f"2. Ethereum: {ethereum_change_rate}")

tether_change_rate = res_parse_list[2]
print(f"3. Tether: {tether_change_rate}")

usd_coin_change_rate = res_parse_list[3]
print(f"4. USD Coin: {usd_coin_change_rate}")

bnb_change_rate = res_parse_list[4]
print(f"5. BNB: {bnb_change_rate}")

xrp_change_rate = res_parse_list[5]
print(f"6. XRP: {xrp_change_rate}")

binance_usd_change_rate = res_parse_list[6]
print(f"7. Binance USD: {binance_usd_change_rate}")

cardano_change_rate = res_parse_list[7]
print(f"8. Cardano: {cardano_change_rate}")

solana_change_rate = res_parse_list[8]
print(f"9. Solana: {solana_change_rate}")

doge_change_rate = res_parse_list[9]
print(f"10. Dogecoin: {doge_change_rate} \n")

def what_coin():
    index = input("What coin do you want to buy? ")
    if index == "Bitcoin":
        answer_bitcoin = input("You want buy Bitcoin? ")
        if answer_bitcoin == "Yes":
            print(f"Bitcoin: {bitcoin_change_rate}")
        elif answer_bitcoin == "No":
            print("You don't want Bitcoin")

    if index == "Ethereum":
        answer_ethereum = input("You want buy Ethereum? ")
        if answer_ethereum == "Yes":
            print(f"Ethereum: {ethereum_change_rate}")
        elif answer_ethereum == "No":
            print("You don't want Ethereum")

    if index == "Tether":
        answer_tether = input("You want buy Tether? ")
        if answer_tether == "Yes":
            print(f"Tether: {tether_change_rate}")
        elif answer_tether == "No":
            print("You don't want Tether")

    if index == "USD Coin":
        answer_usd_coin = input("You want buy USD Coin? ")
        if answer_usd_coin == "Yes":
            print(f"USD Coin: {usd_coin_change_rate}")
        elif answer_usd_coin == "No":
            print("You don't want USD Coin")

    if index == "BNB":
        answer_bnb = input("You want buy BNB? ")
        if answer_bnb == "Yes":
            print(f"BNB: {bnb_change_rate}")
        elif answer_bnb == "No":
            print("You don't want BNB")

    if index == "XRP":
        answer_xrp = input("You want buy XRP? ")
        if answer_xrp == "Yes":
            print(f"XRP: {xrp_change_rate}")
        elif answer_xrp == "No":
            print("You don't want XRP")

    if index == "Binance USD":
        answer_binance_usd = input("You want buy Binance USD? ")
        if answer_binance_usd == "Yes":
            print(f"Binance USD: {binance_usd_change_rate}")
        elif answer_binance_usd == "No":
            print("You don't want Binance USD")

    if index == "Cardano":
        answer_cardano = input("You want buy Cardano? ")
        if answer_cardano == "Yes":
            print(f"Cardano: {cardano_change_rate}")
        elif answer_cardano == "No":
            print("You don't want Cardano")

    if index == "Solana":
        answer_solana = input("You want buy Solana? ")
        if answer_solana == "Yes":
            print(f"Solana: {solana_change_rate}")
        elif answer_solana == "No":
            print("You don't want Solana")

    if index == "Dogecoin":
        answer_doge = input("You want buy Dogecoin? ")
        if answer_doge == "Yes":
            print(f"Dogecoin: {doge_change_rate}")
        elif answer_doge == "No":
            print("You don't want Dogecoin")

what_coin()