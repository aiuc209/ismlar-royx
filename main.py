def ismlar_royxati(ismlar):
    yangi_ismlar = []
    for ism in ismlar:
        yangi_ism = ""
        for harf in ism:
            yangi_ism += harf + "."
        yangi_ismlar.append(yangi_ism[:-1])
    return yangi_ismlar

ismlar = ["Ali", "Vali", "Javohir"]
print(ismlar_royxati(ismlar))
