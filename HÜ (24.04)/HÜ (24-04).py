# max.muster@example.org


email = "max.muster@example.org"


user, domain = email.split("@")


vorname, nachname = user.split(".")


vorname = vorname.capitalize()
nachname = nachname.capitalize()


print(f"Name: {vorname} {nachname}")
print(f"Domain: {domain}")