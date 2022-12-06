from pathlib import Path

p=Path("C:/Users/hugoc/Desktop/M1 MIAGE/Semestre 1/Cryptographie et Sécurité/Crypto/Sprint/livres/indices/1a82884636398e16bc71735eaa07b62fc383f821023a8d771f35281311bee729")

if p.is_file():
    data = p.read_bytes()
    print(data)
    open("1-10.txt", "wb+").write(data)