from RPG_stats import Stats
from fileReader import statFileRead


statList = statFileRead ("RPG\statFile.txt")

#Base Race Stats
class Races:
    '''
    HP,Mana,
    Reg,Mreg,
    AD,MD,MS,
    Def,MR,
    CD,Crit,Gou,Pen,
    STA,LS,Ten,AS,EN
    '''
    Horned = Stats(statList[0].HP,statList[0].Mana,
                   statList[0].AD,statList[0].MD,
                   statList[0].Def,statList[0].MR,statList[0].MS,
                   statList[0].Reg,statList[0].Mreg,
                   statList[0].CD,statList[0].Crit,statList[0].Gou,statList[0].Pen,
                   statList[0].STA,statList[0].LS,statList[0].Ten,statList[0].AS,statList[0].EN)

    Beast = Stats(statList[1].HP,statList[1].Mana,
                   statList[1].AD,statList[1].MD,
                   statList[1].Def,statList[1].MR,statList[1].MS,
                   statList[1].Reg,statList[1].Mreg,
                   statList[1].CD,statList[1].Crit,statList[1].Gou,statList[1].Pen,
                   statList[1].STA,statList[1].LS,statList[1].Ten,statList[1].AS,statList[1].EN)

    Elf = Stats(statList[2].HP,statList[2].Mana,
                   statList[2].AD,statList[2].MD,
                   statList[2].Def,statList[2].MR,statList[2].MS,
                   statList[2].Reg,statList[2].Mreg,
                   statList[2].CD,statList[2].Crit,statList[2].Gou,statList[2].Pen,
                   statList[2].STA,statList[2].LS,statList[2].Ten,statList[2].AS,statList[2].EN)

    Draconic = Stats(statList[3].HP,statList[3].Mana,
                   statList[3].AD,statList[3].MD,
                   statList[3].Def,statList[3].MR,statList[3].MS,
                   statList[3].Reg,statList[3].Mreg,
                   statList[3].CD,statList[3].Crit,statList[3].Gou,statList[3].Pen,
                   statList[3].STA,statList[3].LS,statList[3].Ten,statList[3].AS,statList[3].EN)

    Human = Stats(statList[4].HP,statList[4].Mana,
                   statList[4].AD,statList[4].MD,
                   statList[4].Def,statList[4].MR,statList[4].MS,
                   statList[4].Reg,statList[4].Mreg,
                   statList[4].CD,statList[4].Crit,statList[4].Gou,statList[4].Pen,
                   statList[4].STA,statList[4].LS,statList[4].Ten,statList[4].AS,statList[4].EN)

    Fae = Stats(statList[5].HP,statList[5].Mana,
                   statList[5].AD,statList[5].MD,
                   statList[5].Def,statList[5].MR,statList[5].MS,
                   statList[5].Reg,statList[5].Mreg,
                   statList[5].CD,statList[5].Crit,statList[5].Gou,statList[5].Pen,
                   statList[5].STA,statList[5].LS,statList[5].Ten,statList[5].AS,statList[5].EN)

    Budgie = Stats(statList[6].HP,statList[6].Mana,
                   statList[6].AD,statList[6].MD,
                   statList[6].Def,statList[6].MR,statList[6].MS,
                   statList[6].Reg,statList[6].Mreg,
                   statList[6].CD,statList[6].Crit,statList[6].Gou,statList[6].Pen,
                   statList[6].STA,statList[6].LS,statList[6].Ten,statList[6].AS,statList[6].EN)

    Myst = Stats(statList[7].HP,statList[7].Mana,
                   statList[7].AD,statList[7].MD,
                   statList[7].Def,statList[7].MR,statList[7].MS,
                   statList[7].Reg,statList[7].Mreg,
                   statList[7].CD,statList[7].Crit,statList[7].Gou,statList[7].Pen,
                   statList[7].STA,statList[7].LS,statList[7].Ten,statList[7].AS,statList[7].EN)

    Giant = Stats(statList[8].HP,statList[8].Mana,
                   statList[8].AD,statList[8].MD,
                   statList[8].Def,statList[8].MR,statList[8].MS,
                   statList[8].Reg,statList[8].Mreg,
                   statList[8].CD,statList[8].Crit,statList[8].Gou,statList[8].Pen,
                   statList[8].STA,statList[8].LS,statList[8].Ten,statList[8].AS,statList[8].EN)

    Tanuki = Stats(statList[9].HP,statList[9].Mana,
                   statList[9].AD,statList[9].MD,
                   statList[9].Def,statList[9].MR,statList[9].MS,
                   statList[9].Reg,statList[9].Mreg,
                   statList[9].CD,statList[9].Crit,statList[9].Gou,statList[9].Pen,
                   statList[9].STA,statList[9].LS,statList[9].Ten,statList[9].AS,statList[9].EN)

    Goblin = Stats(statList[10].HP,statList[10].Mana,
                   statList[10].AD,statList[10].MD,
                   statList[10].Def,statList[10].MR,statList[10].MS,
                   statList[10].Reg,statList[10].Mreg,
                   statList[10].CD,statList[10].Crit,statList[10].Gou,statList[10].Pen,
                   statList[10].STA,statList[10].LS,statList[10].Ten,statList[10].AS,statList[10].EN)

    Druid = Stats(statList[11].HP,statList[11].Mana,
                   statList[11].AD,statList[11].MD,
                   statList[11].Def,statList[11].MR,statList[11].MS,
                   statList[11].Reg,statList[11].Mreg,
                   statList[11].CD,statList[11].Crit,statList[11].Gou,statList[11].Pen,
                   statList[11].STA,statList[11].LS,statList[11].Ten,statList[11].AS,statList[11].EN)

