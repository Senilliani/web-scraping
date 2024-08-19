import re
import requests
from colorama import Fore

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, content)
sin_repetir = list(set(maquinas_repetidas))

maquinas_final = []

for maquina in sin_repetir:
    titulo_maquina = maquina.replace("/entry/", "")
    maquinas_final.append(titulo_maquina)
    print(titulo_maquina)


maquina_noob = "noob-1"
existe_noob = False

for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break

color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW

if existe_noob == True:
    print("\n" + color_verde + "No hay máquina nueva")
else:
    print("\n" + color_amarillo + "Máquina nueva!")

