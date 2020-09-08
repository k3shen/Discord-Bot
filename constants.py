import os

petxp=[ 100, 110, 120, 130, 145, 160, 175, 190, 210, 230,
        250, 275, 300, 330, 360, 400, 440, 490, 540, 600,
        660, 730, 800, 880, 960, 1050, 1150, 1260, 1380, 1510,
        1650, 1800, 1960, 2130, 2310, 2500, 2700, 2920, 3160, 3420,
        3700, 4000, 4350, 4750, 5200, 5700, 6300, 7000, 7800, 8700,
        9700, 10800, 12000, 13300, 14700, 16200, 17800, 19500, 21300, 23200,
        25200, 27400, 29800, 32400, 35200, 38200, 41400, 44800, 48400, 52200,
        56200, 60400, 64800, 69400, 74200, 79200, 84700, 90700, 97200, 104200,
        111700, 119700, 128200, 137200, 146700, 156700, 167700, 179700, 192700, 206700,
        221700, 237700, 254700, 272700, 291700, 311700, 333700, 357700, 383700, 411700,
        441700, 476700, 516700, 561700, 611700, 666700, 726700, 791700, 861700, 936700,
        1016700, 1101700, 1191700, 1286700, 1386700, 1496700, 1616700, 1746700, 1886700]

skillxp=[0,50, 125, 200, 300, 500, 750, 1000, 1500, 2000, 3500,
         5000, 7500, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000,
         300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000,
         1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000,
         2300000, 2400000, 2500000, 2600000, 2750000, 2900000, 3100000, 3400000, 3700000, 4000000]

runecraftingxp=[0, 50, 100, 125, 160, 200, 250, 315, 400, 500, 625,
                 785, 1000, 1250, 1600, 2000, 2465, 3125, 4000, 5000, 6200,
                 7800, 9800, 12200, 15300,19200]

talismanreforges = ['Bizarre','Ominous','Simple','Strange','Pleasant',
                    'Shiny','Vivid','Pretty','Itchy','Keen','Unpleasant','Superior',
                    'Forceful', 'Hurtful', 'Strong', 'Demonic', 'Zealous', 'Godly',
                    'Bloody','Silky']

catacombslevel = [0, 4, 8, 12, 16, 20, 25, 30, 35, 40, 45, 51, 57, 63, 69, 75, 82, 89, 96, 103, 110, 118, 126, 134,
                  142, 150, 159, 168, 177, 186, 195, 205, 215, 225, 235, 245, 256, 267, 278, 289, 300, 312, 324,
                  336, 348, 360, 373, 386, 399, 412, 425]

key = str(os.environ['API'])

token = str(os.environ['Bot_Token'])

dbtoken = str(os.environ['DBKey'])

pages = []

pagerefresh = 0
