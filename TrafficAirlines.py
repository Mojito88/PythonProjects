#! /usr/bin/python3

RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CLEAN = '\033[0m'


dublino = RED + "0" + CLEAN
londra = RED + "0" + CLEAN
berlino = RED + "0" + CLEAN
praga = RED + "0" + CLEAN
parigi = RED + "0" + CLEAN
lisbona = RED + "0" + CLEAN
roma = RED + "0" + CLEAN
madrid = RED + "0" + CLEAN




map = f"""
                .  xx/             xxxx   ((xxxxxx        x  *xxxx xxxxxxxxxxx.(
                 /xxxxx*                // #xxxxxx       xxxxx/xxxxxxxxxxxxxxx. 
                 (/xxx                (xx    xxxxx(      /xxxxxxxxxxxxxxxxxxxxxx
            (xxx xxxxx               xx% (x  xx          xxxxxxxxxxxxxxxxxxxxxx
         *xxxxx/  # xxx.              (xx  x  /    xxxxxxxxxxx*xxxxxxxxxxxxxxxxx
          x{dublino}xxx     xxxx*              /xxxxxxx//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        *xxxxx    xxxxxxx (       xx/xxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                  xx xxx{londra}xx     xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                xxxxxx xxx  *xxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxx.xxxxxxxxxxxxxxx
                           xxxxxxxxxxxxx{berlino}xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxx
                 ./  xxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxx(xx xxxxxxxxxxxx
                 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxx/x{praga}xxx#xxxxxxxxxxxxxxx 
                   *xxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxx(xxxxxxxxxxxxxxxx 
                    *xxxxxxxxxxxxxxxxxxxxx(xxxxxxxxx/xxxxx*xxxxxxxxxxxxxxxxxxx  
                     #xxxx{parigi}xxxxxxxxxxxxxxxxxxxx/ *xxxxxxxxxxxxxxx#xxxxxxxxxxxx  
       x            /xxxxxxxxxxxxxxxxxxxxxxxxx(     xxxxxxxx&xxxxxxxxxxxxxxxx   
     xxxxxxxxxxxxx /xxxxxxxxxxxxxxxxx(     xxxxxx/     /xxx#xxxxxxxxxxxxxx*xxxxx
     xxxxxxxxxxxxxxxxxxxx xxx            /  .xxxxx*         /xxxxxxxxxxxxxx xx  
     xxxxxxxxxxxxxxxxxxxxxxxx           xx     x{roma}xxxxxx       xx#xxxxxx(    xxxx
   /xxxxxxxxxxxxxxxxxxxx                 x         xxxxxx(xx  /x(xxxxx      / xx
  .x{lisbona}xx/xxxxxxxxxxxxxx        x(        xx             xx*  x   &/xxxx /x     * 
    xxx.xxxxxx{madrid}xxxxxxx   x              x               x        ( xxxx/       .
     x xxxxxxxxxxxxx                             xx*xxx             x xx        
        /xxx *xx.x                        xx         xx                     (( (
         x             xxxxxxxxxxxxxxxxxxxxxx                                   
"""

print(map)

# obbiettivo : far passare ogni aereo per la strada più breve + sempre scalo del paese più vicino

print("\n Areoporti: [ Lisbona Madrid Parigi Berlino Praga Roma Londra Dublino ] \n")
partenza = input("Inserire l'areoporto di partenza: ")
arrivo = input("\nInserire l'areoporto d'arrivo: ")
partenza = partenza.lower()
arrivo = arrivo.lower()



#* Lisbona 1
#  Madrid 2
#  Parigi 3
#  Berlino 4
#  Praga 5
#  Roma 6
#  Londra 7
#  Dublino 8

travel = []

if partenza == arrivo:
    print("Destinazione e/o partenza non validi.")
    exit()



scalo1 = ""


if partenza == "lisbona": #1
    scalo1 = "madrid"
if partenza == "madrid": #2
    scalo1 = "lisbona"
if partenza == "parigi": #3
    scalo1 = "roma"
if partenza == "berlino": #4
    scalo1 = "praga"
if partenza == "praga": #5
    scalo1 = "berlino"
if partenza == "roma": #6
    scalo1 = "parigi"
if partenza == "londra": #7
    scalo1 = "dublino"
if partenza == "dublino": #8
    scalo1 = "londra"

scalo2 = ""

if  arrivo == "lisbona": #1
    scalo1 = "madrid"
if  arrivo == "madrid": #2
    scalo2 = "lisbona"
if  arrivo == "parigi": #3
    scalo2 = "roma"
if  arrivo == "berlino": #4
    scalo2 = "praga"
if  arrivo == "praga": #5
    scalo2 = "berlino"
if  arrivo == "roma": #6
    scalo2 = "parigi"
if  arrivo == "londra": #7
    scalo2 = "dublino"
if  arrivo == "dublino": #8
    scalo2 = "londra"


travel.append(partenza)
travel.append(scalo1)
travel.append(scalo2)
travel.append(arrivo)


print(f"""
     Viaggio:

     {RED + travel[0] + CLEAN} ----> {RED + travel[1] + CLEAN} ----> {RED + travel[2] + CLEAN} ----> {RED + travel[3] + CLEAN}    

""")
