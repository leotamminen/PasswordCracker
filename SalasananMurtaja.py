import pyautogui
import random
import time

merkit = "0123456789"
merkit_listana = list(merkit)

oikea_koodi = pyautogui.password("Syötä koodi: ")

start = time.time()

a = 0
for i in range(1000):
    a += (i**100)


arvattu_koodi = ""
kaytetyt_koodit = []

# Aloitus

ensimmainen_arvaus = random.choices(merkit_listana, k=len(oikea_koodi))
kaytetyt_koodit.append(str(ensimmainen_arvaus))


while(arvattu_koodi != oikea_koodi):

    if str(arvattu_koodi) not in kaytetyt_koodit:

        arvattu_koodi = random.choices(merkit_listana, k=len(oikea_koodi))

        print("<===============" + str(arvattu_koodi) + "===============>")

        kaytetyt_koodit.append(str(arvattu_koodi))



    if(arvattu_koodi == list(oikea_koodi)):
        koodi_yhdistettyna = "".join(arvattu_koodi)
        print(f"Koodi oli {koodi_yhdistettyna}!")
        end = time.time()
        print("Koodin murtamisessa kesti", round(end - start, 2), "sekuntia!")
        break