import requests
import time
time.sleep(2)
nomedosite = input("qual o site voce deseja fazer a requisicao?: ")
requisiçao = requests.get(nomedosite)
print("a cituaçao do ", nomedosite, "esta", requisiçao)
