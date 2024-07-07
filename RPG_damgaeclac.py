from RPG_stats import Stats
from RPG_raceStats import Races
from RPG_stat_growth import statgrowth
from RPG_class_growth import Classes
import RPG_statcalc



def damcalc ():
    Dam_type = input("Physical or Magic damage? (p/m): ")

    Stats_1 = RPG_statcalc.RPGcalc.RaceStat()
    HP_1 =  Stats_1[0]
    if Dam_type == "p":
        Attack_1 = Stats_1[4]
        Resist_1 = Stats_1[7]
        Lethal = Stats_1[11]
    elif Dam_type == "m":
        Attack_1 = Stats_1[5]
        Resist_1 = Stats_1[8]
        Lethal = Stats_1[12]

    Stats_2 = RPG_statcalc.RPGcalc.RaceStat()
    HP_2 =  Stats_2[0]
    if Dam_type == "p":
        Attack_2 = Stats_2[4]
        Resist_2 = Stats_2[7]
        Resist_2 = Resist_2 - Lethal
    elif Dam_type == "m":
        Attack_2 = Stats_2[5]
        Resist_2 = Stats_2[8]
        Resist_2 = Resist_2 - Lethal

    Dam = Attack_1 * (100/(100+Resist_2))
    Remain_HP = HP_2 - Dam
    percDam = Dam / HP_2
    txt = ("Attack:\t{:.2f}\nLethal:\t{:.2f}\nResist:\t{:.2f}\nHP:\t{:.2f}\nDamage:\t{:.2f}\n% Dealt:\t{:.2f}\nRemaining HP:\t{:.2f}")
    print(txt.format(Attack_1, Lethal, Resist_2, HP_2, Dam, percDam, Remain_HP))

damcalc()

'''
    HP = float(input("HP of Target: "))
    Attack = float(input("Attack Damage: "))
    Resist = float(input("Resists: "))'''
