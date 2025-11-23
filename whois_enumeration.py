import whois

domain_name = str(input("Dime un nombre de dominio: "))
response = whois.whois(domain_name)

print(response)
