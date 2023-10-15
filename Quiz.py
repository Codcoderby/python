import random

suallar = {
    "Azerbaycan'nin paytaxti haradir?": "Baki",
    "Fransa'nın paytaxti haradir?": "Paris",
    "İngiltere'nin paytaxti haradir?": "Londra",
    "Almanya'nın paytaxti haradir?": "Berlin",
    "İtalya'nın paytaxti haradir?": "Roma",
    "İspanya'nın paytaxti haradir?": "Madrid",
    "Çin'in paytaxti haradir?": "Pekin",
    "Rusya'nın paytaxti haradir?": "Moskova",
    "Japonya'nın paytaxti haradir?": "Tokyo",
    "Hindistan'ın paytaxti haradir?": "Yeni Delhi",
}

skor = 0

suallar_list = list(suallar.keys())
random.shuffle(suallar_list)

for sual in suallar_list[:10]:
    cavab = input(sual + " ")
    if cavab.lower() == suallar[sual].lower():
        print("Dogru!")
        skor += 10
    else:
        print("Yalnis. Dogru cavab: " + suallar[sual])
        skor -= 5

print("Oyun bitdi. Umumi xaliniz:", skor)
