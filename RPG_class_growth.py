from RPG_stat_growth import statgrowth
from fileReader import statFileRead
#Controls our stat growth numbers

classGrowth = statFileRead("RPG\classFile.txt")
class Classes:
    """
    HP,Mana,
    Reg,Mreg,
    AD,AP,MS
    Def,MR,
    CD,Crit,Gouge,Pen
    STA,LS,TEN,AS,EN
    """

    Base = statgrowth(classGrowth[0].HP,classGrowth[0].Mana,
                   classGrowth[0].AD,classGrowth[0].MD,
                   classGrowth[0].Def,classGrowth[0].MR,classGrowth[0].MS,
                   classGrowth[0].Reg,classGrowth[0].Mreg,
                   classGrowth[0].CD,classGrowth[0].Crit,classGrowth[0].Gou,classGrowth[0].Pen,
                   classGrowth[0].STA,classGrowth[0].LS,classGrowth[0].Ten,classGrowth[0].AS,classGrowth[0].EN)
    
    Tank = statgrowth(classGrowth[1].HP,classGrowth[1].Mana,
                   classGrowth[1].AD,classGrowth[1].MD,
                   classGrowth[1].Def,classGrowth[1].MR,classGrowth[1].MS,
                   classGrowth[1].Reg,classGrowth[1].Mreg,
                   classGrowth[1].CD,classGrowth[1].Crit,classGrowth[1].Gou,classGrowth[1].Pen,
                   classGrowth[1].STA,classGrowth[1].LS,classGrowth[1].Ten,classGrowth[1].AS,classGrowth[1].EN)

    Fighter = statgrowth(classGrowth[2].HP,classGrowth[2].Mana,
                   classGrowth[2].AD,classGrowth[2].MD,
                   classGrowth[2].Def,classGrowth[2].MR,classGrowth[2].MS,
                   classGrowth[2].Reg,classGrowth[2].Mreg,
                   classGrowth[2].CD,classGrowth[2].Crit,classGrowth[2].Gou,classGrowth[2].Pen,
                   classGrowth[2].STA,classGrowth[2].LS,classGrowth[2].Ten,classGrowth[2].AS,classGrowth[2].EN)

    Mage = statgrowth(classGrowth[3].HP,classGrowth[3].Mana,
                   classGrowth[3].AD,classGrowth[3].MD,
                   classGrowth[3].Def,classGrowth[3].MR,classGrowth[3].MS,
                   classGrowth[3].Reg,classGrowth[3].Mreg,
                   classGrowth[3].CD,classGrowth[3].Crit,classGrowth[3].Gou,classGrowth[3].Pen,
                   classGrowth[3].STA,classGrowth[3].LS,classGrowth[3].Ten,classGrowth[3].AS,classGrowth[3].EN)

    Assassin = statgrowth(classGrowth[4].HP,classGrowth[4].Mana,
                   classGrowth[4].AD,classGrowth[4].MD,
                   classGrowth[4].Def,classGrowth[4].MR,classGrowth[4].MS,
                   classGrowth[4].Reg,classGrowth[4].Mreg,
                   classGrowth[4].CD,classGrowth[4].Crit,classGrowth[4].Gou,classGrowth[4].Pen,
                   classGrowth[4].STA,classGrowth[4].LS,classGrowth[4].Ten,classGrowth[4].AS,classGrowth[4].EN)

    Ranger = statgrowth(classGrowth[5].HP,classGrowth[5].Mana,
                   classGrowth[5].AD,classGrowth[5].MD,
                   classGrowth[5].Def,classGrowth[5].MR,classGrowth[5].MS,
                   classGrowth[5].Reg,classGrowth[5].Mreg,
                   classGrowth[5].CD,classGrowth[5].Crit,classGrowth[5].Gou,classGrowth[5].Pen,
                   classGrowth[5].STA,classGrowth[5].LS,classGrowth[5].Ten,classGrowth[5].AS,classGrowth[5].EN)

    Enchanter = statgrowth(classGrowth[6].HP,classGrowth[6].Mana,
                   classGrowth[6].AD,classGrowth[6].MD,
                   classGrowth[6].Def,classGrowth[6].MR,classGrowth[6].MS,
                   classGrowth[6].Reg,classGrowth[6].Mreg,
                   classGrowth[6].CD,classGrowth[6].Crit,classGrowth[6].Gou,classGrowth[6].Pen,
                   classGrowth[6].STA,classGrowth[6].LS,classGrowth[6].Ten,classGrowth[6].AS,classGrowth[6].EN)

    Warden = statgrowth(classGrowth[7].HP,classGrowth[7].Mana,
                   classGrowth[7].AD,classGrowth[7].MD,
                   classGrowth[7].Def,classGrowth[7].MR,classGrowth[7].MS,
                   classGrowth[7].Reg,classGrowth[7].Mreg,
                   classGrowth[7].CD,classGrowth[7].Crit,classGrowth[7].Gou,classGrowth[7].Pen,
                   classGrowth[7].STA,classGrowth[7].LS,classGrowth[7].Ten,classGrowth[7].AS,classGrowth[7].EN)
    
    Adventurer = statgrowth(classGrowth[8].HP,classGrowth[8].Mana,
                   classGrowth[8].AD,classGrowth[8].MD,
                   classGrowth[8].Def,classGrowth[8].MR,classGrowth[8].MS,
                   classGrowth[8].Reg,classGrowth[8].Mreg,
                   classGrowth[8].CD,classGrowth[8].Crit,classGrowth[8].Gou,classGrowth[8].Pen,
                   classGrowth[8].STA,classGrowth[8].LS,classGrowth[8].Ten,classGrowth[8].AS,classGrowth[8].EN)
    
    Bard = statgrowth(classGrowth[9].HP,classGrowth[9].Mana,
                   classGrowth[9].AD,classGrowth[9].MD,
                   classGrowth[9].Def,classGrowth[9].MR,classGrowth[9].MS,
                   classGrowth[9].Reg,classGrowth[9].Mreg,
                   classGrowth[9].CD,classGrowth[9].Crit,classGrowth[9].Gou,classGrowth[9].Pen,
                   classGrowth[9].STA,classGrowth[9].LS,classGrowth[9].Ten,classGrowth[9].AS,classGrowth[9].EN)
    
    Hunter = statgrowth(classGrowth[10].HP,classGrowth[10].Mana,
                   classGrowth[10].AD,classGrowth[10].MD,
                   classGrowth[10].Def,classGrowth[10].MR,classGrowth[10].MS,
                   classGrowth[10].Reg,classGrowth[10].Mreg,
                   classGrowth[10].CD,classGrowth[10].Crit,classGrowth[10].Gou,classGrowth[10].Pen,
                   classGrowth[10].STA,classGrowth[10].LS,classGrowth[10].Ten,classGrowth[10].AS,classGrowth[10].EN)
