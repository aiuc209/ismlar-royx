import pytest

def ismni_ozgartir(ism):
    yangi_ism = ""
    for i in ism:
        yangi_ism += i + "."
    return yangi_ism[:-1]

@pytest.mark.parametrize("ism, natija", [
    ("Ali", "A.l.i"),
    ("Vali", "V.a.l.i"),
    ("Sardor", "S.a.r.d.o.r")
])
def test_ismni_ozgartir(ism, natija):
    assert ismni_ozgartir(ism) == natija
