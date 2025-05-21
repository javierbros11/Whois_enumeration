import whois

domain_name = "example.com"
response = whois.whois(domain_name)

print(response)