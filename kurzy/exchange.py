import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')
print("server odpovedel", r.status_code)


lines = r.text.split('\n')
print('Kurzy pro den', lines[0].split(' ')[0])

line_eur = ""
for line in lines:
    if "EUR" in line:
        line_eur = line
        break

rate_str = line_eur.split('|')[-1]
rate = float(rate_str.replace(',','.'))

print("Kurz euro je", rate)


while True:
    while True:
        q = input("EUR -> CZK (1) / CZK -> EUR (2), q (quit) ")

        if (q == "q"):
            exit(0)
        try: 
            currency = float(q)
            break
        except ValueError:
            print("Neplatny vstup, zadej 1 nebo 2")

    if(currency == 1):
        while True:
            s = input("Kolik mas EUR? ")
            try:
                value_in = float(s)
                break
            except ValueError:
                print("Neplatný vstup, zadej číslo.")
        value_out = value_in * rate

        print (f"Tak to mas {value_out:.02f} CZK")
    else:
        while True:
            s = input("Kolik mas CZK? ")
            try:
                value_in = float(s)
                break
            except ValueError:
                print("Neplatný vstup, zadej číslo.")
        value_out = value_in / rate

        print (f"Tak to mas {value_out:.02f} EUR")