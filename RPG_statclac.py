from RPG_stats import Stats
from RPG_raceStats import Races
from RPG_stat_growth import statgrowth
from RPG_class_growth import Classes



class RPGcalc :

#HP,Mana,Reg,Mreg,AD,AP,MS
#Def,MR,CD,Crit,Gouge,Pen
#STA,LS,TEN,AS,EN

    def RaceStat ():

        rText = """What Race is your character?: 
                     \n1: Horned | 2: Beast | 3: Elf
                         \r4: Draconic | 5: Human | 6: Fae
                         \r7: Budgie | 8: Myst | 9: Giant
                         \r10: Tanuki | 11: Goblin | 12: Druid\n"""
        
        cText = """"What Class is your character?: 
                     \n1: Tank | 2: Fighter | 3: Mage
                         \r4: Assassin | 5: Ranger | 6: Enchanter
                         \r7: Warden | 8: Adventurer | 9: Bard
                         \r10: Hunter\n"""
        
        Race = int(input(rText))
    
        LV = int(input("What Level is your character?: \n"))
    
        Class = int(input(cText))

        if Race == 1:
            Race = "Horned"
            HP = Races.Horned.HP
            Mana = Races.Horned.Mana
            AD = Races.Horned.AD 
            MD = Races.Horned.MD
            Def = Races.Horned.Def
            MR = Races.Horned.MR
            MS = Races.Horned.MS 
            Reg = Races.Horned.Reg
            MReg = Races.Horned.Mreg 
            CD = Races.Horned.CD
            Crit = Races.Horned.Crit
            Gouge = Races.Horned.Gou 
            Pen = Races.Horned.Pen 
            STA = Races.Horned.STA 
            LS = Races.Horned.LS 
            TEN = Races.Horned.Ten 
            AS = Races.Horned.AS 
            EN = Races.Horned.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 2:
            Race = "Beast"
            HP = Races.Beast.HP
            Mana = Races.Beast.Mana
            AD = Races.Beast.AD 
            MD = Races.Beast.MD 
            Def = Races.Beast.Def
            MR = Races.Beast.MR 
            MS = Races.Beast.MS
            Reg = Races.Beast.Reg
            MReg = Races.Beast.Mreg 
            CD = Races.Beast.CD
            Crit = Races.Beast.Crit
            Gouge = Races.Beast.Gou 
            Pen = Races.Beast.Pen 
            STA = Races.Beast.STA 
            LS = Races.Beast.LS 
            TEN = Races.Beast.Ten 
            AS = Races.Beast.AS 
            EN = Races.Beast.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 3:
            Race = "Elf"
            HP = Races.Elf.HP
            Mana = Races.Elf.Mana
            AD = Races.Elf.AD 
            MD = Races.Elf.MD 
            Def = Races.Elf.Def
            MR = Races.Elf.MR 
            MS = Races.Elf.MS
            Reg = Races.Elf.Reg
            MReg = Races.Elf.Mreg 
            CD = Races.Elf.CD
            Crit = Races.Elf.Crit
            Gouge = Races.Elf.Gou 
            Pen = Races.Elf.Pen 
            STA = Races.Elf.STA 
            LS = Races.Elf.LS 
            TEN = Races.Elf.Ten 
            AS = Races.Elf.AS 
            EN = Races.Elf.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 4:
            Race = "Draconic"
            HP = Races.Draconic.HP
            Mana = Races.Draconic.Mana
            AD = Races.Draconic.AD 
            MD = Races.Draconic.MD 
            Def = Races.Draconic.Def
            MR = Races.Draconic.MR 
            MS = Races.Draconic.MS
            Reg = Races.Draconic.Reg
            MReg = Races.Draconic.Mreg 
            CD = Races.Draconic.CD
            Crit = Races.Draconic.Crit
            Gouge = Races.Draconic.Gou 
            Pen = Races.Draconic.Pen 
            STA = Races.Draconic.STA 
            LS = Races.Draconic.LS 
            TEN = Races.Draconic.Ten 
            AS = Races.Draconic.AS 
            EN = Races.Draconic.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 5:
            Race = "Human"
            HP = Races.Human.HP
            Mana = Races.Human.Mana
            AD = Races.Human.AD 
            MD = Races.Human.MD 
            Def = Races.Human.Def
            MR = Races.Human.MR 
            MS = Races.Human.MS
            Reg = Races.Human.Reg
            MReg = Races.Human.Mreg 
            CD = Races.Human.CD
            Crit = Races.Human.Crit
            Gouge = Races.Human.Gou 
            Pen = Races.Human.Pen 
            STA = Races.Human.STA 
            LS = Races.Human.LS 
            TEN = Races.Human.Ten 
            AS = Races.Human.AS 
            EN = Races.Human.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 6:
            Race = "Fae"
            HP = Races.Fae.HP
            Mana = Races.Fae.Mana
            AD = Races.Fae.AD 
            MD = Races.Fae.MD 
            Def = Races.Fae.Def
            MR = Races.Fae.MR 
            MS = Races.Fae.MS
            Reg = Races.Fae.Reg
            MReg = Races.Fae.Mreg 
            CD = Races.Fae.CD
            Crit = Races.Fae.Crit
            Gouge = Races.Fae.Gou 
            Pen = Races.Fae.Pen 
            STA = Races.Fae.STA 
            LS = Races.Fae.LS 
            TEN = Races.Fae.Ten 
            AS = Races.Fae.AS 
            EN = Races.Fae.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 7:
            Race = "Budgie"
            HP = Races.Budgie.HP
            Mana = Races.Budgie.Mana
            AD = Races.Budgie.AD 
            MD = Races.Budgie.MD 
            Def = Races.Budgie.Def
            MR = Races.Budgie.MR 
            MS = Races.Budgie.MS
            Reg = Races.Budgie.Reg
            MReg = Races.Budgie.Mreg 
            CD = Races.Budgie.CD
            Crit = Races.Budgie.Crit
            Gouge = Races.Budgie.Gou 
            Pen = Races.Budgie.Pen 
            STA = Races.Budgie.STA 
            LS = Races.Budgie.LS 
            TEN = Races.Budgie.Ten 
            AS = Races.Budgie.AS 
            EN = Races.Budgie.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 8:
            Race = "Myst"
            HP = Races.Myst.HP
            Mana = Races.Myst.Mana
            AD = Races.Myst.AD 
            MD = Races.Myst.MD 
            Def = Races.Myst.Def
            MR = Races.Myst.MR 
            MS = Races.Myst.MS
            Reg = Races.Myst.Reg
            MReg = Races.Myst.Mreg 
            CD = Races.Myst.CD
            Crit = Races.Myst.Crit
            Gouge = Races.Myst.Gou 
            Pen = Races.Myst.Pen 
            STA = Races.Myst.STA 
            LS = Races.Myst.LS 
            TEN = Races.Myst.Ten 
            AS = Races.Myst.AS 
            EN = Races.Myst.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 9:
            Race = "Giant"
            HP = Races.Giant.HP
            Mana = Races.Giant.Mana
            AD = Races.Giant.AD 
            MD = Races.Giant.MD 
            Def = Races.Giant.Def
            MR = Races.Giant.MR 
            MS = Races.Giant.MS
            Reg = Races.Giant.Reg
            MReg = Races.Giant.Mreg 
            CD = Races.Giant.CD
            Crit = Races.Giant.Crit
            Gouge = Races.Giant.Gou 
            Pen = Races.Giant.Pen 
            STA = Races.Giant.STA 
            LS = Races.Giant.LS 
            TEN = Races.Giant.Ten 
            AS = Races.Giant.AS 
            EN = Races.Giant.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 10:
            Race = "Tanuki"
            HP = Races.Tanuki.HP
            Mana = Races.Tanuki.Mana
            AD = Races.Tanuki.AD 
            MD = Races.Tanuki.MD 
            Def = Races.Tanuki.Def
            MR = Races.Tanuki.MR 
            MS = Races.Tanuki.MS
            Reg = Races.Tanuki.Reg
            MReg = Races.Tanuki.Mreg 
            CD = Races.Tanuki.CD
            Crit = Races.Tanuki.Crit
            Gouge = Races.Tanuki.Gou 
            Pen = Races.Tanuki.Pen 
            STA = Races.Tanuki.STA 
            LS = Races.Tanuki.LS 
            TEN = Races.Tanuki.Ten 
            AS = Races.Tanuki.AS 
            EN = Races.Tanuki.EN 
            
            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 11:
            Race = "Goblin"
            HP = Races.Goblin.HP
            Mana = Races.Goblin.Mana
            AD = Races.Goblin.AD 
            MD = Races.Goblin.MD 
            Def = Races.Goblin.Def
            MR = Races.Goblin.MR 
            MS = Races.Goblin.MS
            Reg = Races.Goblin.Reg
            MReg = Races.Goblin.Mreg 
            CD = Races.Goblin.CD
            Crit = Races.Goblin.Crit
            Gouge = Races.Goblin.Gou 
            Pen = Races.Goblin.Pen 
            STA = Races.Goblin.STA 
            LS = Races.Goblin.LS 
            TEN = Races.Goblin.Ten 
            AS = Races.Goblin.AS 
            EN = Races.Goblin.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)

        elif Race == 12:
            Race = "Druid"
            HP = Races.Druid.HP
            Mana = Races.Druid.Mana
            AD = Races.Druid.AD 
            MD = Races.Druid.MD 
            Def = Races.Druid.Def
            MR = Races.Druid.MR 
            MS = Races.Druid.MS
            Reg = Races.Druid.Reg
            MReg = Races.Druid.Mreg 
            CD = Races.Druid.CD
            Crit = Races.Druid.Crit
            Gouge = Races.Druid.Gou 
            Pen = Races.Druid.Pen 
            STA = Races.Druid.STA 
            LS = Races.Druid.LS 
            TEN = Races.Druid.Ten 
            AS = Races.Druid.AS 
            EN = Races.Druid.EN 

            #return(HP, Mana, Reg, MReg, AD, MD, MS, Def, MR, CD, Crit, Gouge, Pen, STA, LS, TEN, AS, EN)
        else:
            print("Race not found")



        if Class == 1:
            Class = "Tank"
            HP_g = Classes.Tank.HP_growth
            Mana_g = Classes.Tank.Mana_growth
            AD_g = Classes.Tank.AD_growth
            MD_g = Classes.Tank.MD_growth 
            Def_g = Classes.Tank.Def_growth
            MR_g = Classes.Tank.MR_growth 
            MS_g = Classes.Tank.MS_growth 
            Reg_g = Classes.Tank.Reg_growth
            MReg_g = Classes.Tank.MReg_growth
            CD_g = Classes.Tank.CD_growth
            Crit_g = Classes.Tank.Crit_growth
            Gouge_g = Classes.Tank.Gou_growth 
            Pen_g = Classes.Tank.Pen_growth 
            STA_g = Classes.Tank.STA_growth 
            LS_g = Classes.Tank.LS_growth 
            TEN_g = Classes.Tank.Ten_growth 
            AS_g = Classes.Tank.AS_growth 
            EN_g = Classes.Tank.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 2:
            Class = "Fighter"
            HP_g = Classes.Fighter.HP_growth
            Mana_g = Classes.Fighter.Mana_growth
            Reg_g = Classes.Fighter.Reg_growth
            MReg_g = Classes.Fighter.MReg_growth
            AD_g = Classes.Fighter.AD_growth
            MD_g = Classes.Fighter.MD_growth 
            MS_g = Classes.Fighter.MS_growth 
            Def_g = Classes.Fighter.Def_growth
            MR_g = Classes.Fighter.MR_growth 
            CD_g = Classes.Fighter.CD_growth
            Crit_g = Classes.Fighter.Crit_growth
            Gouge_g = Classes.Fighter.Gou_growth 
            Pen_g = Classes.Fighter.Pen_growth 
            STA_g = Classes.Fighter.STA_growth 
            LS_g = Classes.Fighter.LS_growth 
            TEN_g = Classes.Fighter.Ten_growth 
            AS_g = Classes.Fighter.AS_growth 
            EN_g = Classes.Fighter.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 3:
            Class = "Mage"
            HP_g = Classes.Mage.HP_growth
            Mana_g = Classes.Mage.Mana_growth
            Reg_g = Classes.Mage.Reg_growth
            MReg_g = Classes.Mage.MReg_growth
            AD_g = Classes.Mage.AD_growth
            MD_g = Classes.Mage.MD_growth 
            MS_g = Classes.Mage.MS_growth 
            Def_g = Classes.Mage.Def_growth
            MR_g = Classes.Mage.MR_growth 
            CD_g = Classes.Mage.CD_growth
            Crit_g = Classes.Mage.Crit_growth
            Gouge_g = Classes.Mage.Gou_growth 
            Pen_g = Classes.Mage.Pen_growth 
            STA_g = Classes.Mage.STA_growth 
            LS_g = Classes.Mage.LS_growth 
            TEN_g = Classes.Mage.Ten_growth 
            AS_g = Classes.Mage.AS_growth 
            EN_g = Classes.Mage.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 4:
            Class = "Assassin"
            HP_g = Classes.Assassin.HP_growth
            Mana_g = Classes.Assassin.Mana_growth
            Reg_g = Classes.Assassin.Reg_growth
            MReg_g = Classes.Assassin.MReg_growth
            AD_g = Classes.Assassin.AD_growth
            MD_g = Classes.Assassin.MD_growth 
            MS_g = Classes.Assassin.MS_growth 
            Def_g = Classes.Assassin.Def_growth
            MR_g = Classes.Assassin.MR_growth 
            CD_g = Classes.Assassin.CD_growth
            Crit_g = Classes.Assassin.Crit_growth
            Gouge_g = Classes.Assassin.Gou_growth 
            Pen_g = Classes.Assassin.Pen_growth 
            STA_g = Classes.Assassin.STA_growth 
            LS_g = Classes.Assassin.LS_growth 
            TEN_g = Classes.Assassin.Ten_growth 
            AS_g = Classes.Assassin.AS_growth 
            EN_g = Classes.Assassin.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 5:
            Class = "Ranger"
            HP_g = Classes.Ranger.HP_growth
            Mana_g = Classes.Ranger.Mana_growth
            Reg_g = Classes.Ranger.Reg_growth
            MReg_g = Classes.Ranger.MReg_growth
            AD_g = Classes.Ranger.AD_growth
            MD_g = Classes.Ranger.MD_growth 
            MS_g = Classes.Ranger.MS_growth 
            Def_g = Classes.Ranger.Def_growth
            MR_g = Classes.Ranger.MR_growth 
            CD_g = Classes.Ranger.CD_growth
            Crit_g = Classes.Ranger.Crit_growth
            Gouge_g = Classes.Ranger.Gou_growth 
            Pen_g = Classes.Ranger.Pen_growth 
            STA_g = Classes.Ranger.STA_growth 
            LS_g = Classes.Ranger.LS_growth 
            TEN_g = Classes.Ranger.Ten_growth 
            AS_g = Classes.Ranger.AS_growth 
            EN_g = Classes.Ranger.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 6:
            Class = "Enchanter"
            HP_g = Classes.Enchanter.HP_growth
            Mana_g = Classes.Enchanter.Mana_growth
            Reg_g = Classes.Enchanter.Reg_growth
            MReg_g = Classes.Enchanter.MReg_growth
            AD_g = Classes.Enchanter.AD_growth
            MD_g = Classes.Enchanter.MD_growth 
            MS_g = Classes.Enchanter.MS_growth 
            Def_g = Classes.Enchanter.Def_growth
            MR_g = Classes.Enchanter.MR_growth 
            CD_g = Classes.Enchanter.CD_growth
            Crit_g = Classes.Enchanter.Crit_growth
            Gouge_g = Classes.Enchanter.Gou_growth 
            Pen_g = Classes.Enchanter.Pen_growth 
            STA_g = Classes.Enchanter.STA_growth 
            LS_g = Classes.Enchanter.LS_growth 
            TEN_g = Classes.Enchanter.Ten_growth 
            AS_g = Classes.Enchanter.AS_growth 
            EN_g = Classes.Enchanter.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)


        elif Class == 7:
            Class = "Warden"
            HP_g = Classes.Warden.HP_growth
            Mana_g = Classes.Warden.Mana_growth
            Reg_g = Classes.Warden.Reg_growth
            MReg_g = Classes.Warden.MReg_growth
            AD_g = Classes.Warden.AD_growth
            MD_g = Classes.Warden.MD_growth 
            MS_g = Classes.Warden.MS_growth 
            Def_g = Classes.Warden.Def_growth
            MR_g = Classes.Warden.MR_growth 
            CD_g = Classes.Warden.CD_growth
            Crit_g = Classes.Warden.Crit_growth
            Gouge_g = Classes.Warden.Gou_growth 
            Pen_g = Classes.Warden.Pen_growth 
            STA_g = Classes.Warden.STA_growth 
            LS_g = Classes.Warden.LS_growth 
            TEN_g = Classes.Warden.Ten_growth 
            AS_g = Classes.Warden.AS_growth 
            EN_g = Classes.Warden.Enc_growth 

           #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 8:
            Class = "Adventurer"
            HP_g = Classes.Adventurer.HP_growth
            Mana_g = Classes.Adventurer.Mana_growth
            Reg_g = Classes.Adventurer.Reg_growth
            MReg_g = Classes.Adventurer.MReg_growth
            AD_g = Classes.Adventurer.AD_growth
            MD_g = Classes.Adventurer.MD_growth 
            MS_g = Classes.Adventurer.MS_growth 
            Def_g = Classes.Adventurer.Def_growth
            MR_g = Classes.Adventurer.MR_growth 
            CD_g = Classes.Adventurer.CD_growth
            Crit_g = Classes.Adventurer.Crit_growth
            Gouge_g = Classes.Adventurer.Gou_growth 
            Pen_g = Classes.Adventurer.Pen_growth 
            STA_g = Classes.Adventurer.STA_growth 
            LS_g = Classes.Adventurer.LS_growth 
            TEN_g = Classes.Adventurer.Ten_growth 
            AS_g = Classes.Adventurer.AS_growth 
            EN_g = Classes.Adventurer.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)


        elif Class == 9:
            Class = "Bard"
            HP_g = Classes.Bard.HP_growth
            Mana_g = Classes.Bard.Mana_growth
            Reg_g = Classes.Bard.Reg_growth
            MReg_g = Classes.Bard.MReg_growth
            AD_g = Classes.Bard.AD_growth
            MD_g = Classes.Bard.MD_growth 
            MS_g = Classes.Bard.MS_growth 
            Def_g = Classes.Bard.Def_growth
            MR_g = Classes.Bard.MR_growth 
            CD_g = Classes.Bard.CD_growth
            Crit_g = Classes.Bard.Crit_growth
            Gouge_g = Classes.Bard.Gou_growth 
            Pen_g = Classes.Bard.Pen_growth 
            STA_g = Classes.Bard.STA_growth 
            LS_g = Classes.Bard.LS_growth 
            TEN_g = Classes.Bard.Ten_growth 
            AS_g = Classes.Bard.AS_growth 
            EN_g = Classes.Bard.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        elif Class == 10:
            Class = "Hunter"
            HP_g = Classes.Hunter.HP_growth
            Mana_g = Classes.Hunter.Mana_growth
            Reg_g = Classes.Hunter.Reg_growth
            MReg_g = Classes.Hunter.MReg_growth
            AD_g = Classes.Hunter.AD_growth
            MD_g = Classes.Hunter.MD_growth 
            MS_g = Classes.Hunter.MS_growth 
            Def_g = Classes.Hunter.Def_growth
            MR_g = Classes.Hunter.MR_growth 
            CD_g = Classes.Hunter.CD_growth
            Crit_g = Classes.Hunter.Crit_growth
            Gouge_g = Classes.Hunter.Gou_growth 
            Pen_g = Classes.Hunter.Pen_growth 
            STA_g = Classes.Hunter.STA_growth 
            LS_g = Classes.Hunter.LS_growth 
            TEN_g = Classes.Hunter.Ten_growth 
            AS_g = Classes.Hunter.AS_growth 
            EN_g = Classes.Hunter.Enc_growth 

            #return(HP_g, Mana_g, Reg_g, MReg_g, AD_g, MD_g, MS_g, Def_g, MR_g, CD_g, Crit_g, Gouge_g, Pen_g, STA_g, LS_g, TEN_g, AS_g, EN_g)

        else:
            print("No class found")
        

        F_HP = HP + HP_g*(LV-1)
        F_Mana = Mana + Mana_g*(LV-1)
        F_Reg = Reg + Reg_g*(LV-1)
        F_MReg = MReg + MReg_g*(LV-1)
        F_AD = AD + AD_g*(LV-1)
        F_MD = MD + MD_g*(LV-1)
        F_MS = MS + MS_g*(LV-1)
        F_Def = Def + Def_g*(LV-1)
        F_MR = MR + MR_g*(LV-1)
        F_CD = CD + CD_g*(LV-1)
        F_Crit = Crit + Crit_g*(LV-1)
        F_Gouge = Gouge + Gouge_g*(LV-1)
        F_Pen = Pen + Pen_g*(LV-1)
        F_STA = STA + STA_g*(LV-1)
        F_LS = LS + LS_g*(LV-1)
        F_TEN = TEN + TEN_g*(LV-1)
        F_AS = AS + AS_g*(LV-1)
        F_EN = EN + EN_g*(LV-1)

        sumText = f"Your Character is a Lv {LV} {Race} {Class}:"
        print("--" * 25)
        print(sumText)
        F_Stats = [F_HP, F_Mana, F_Reg, F_MReg, F_AD, F_MD, F_MS, F_Def, F_MR, F_CD, F_Crit, F_Gouge, F_Pen, F_STA, F_LS, F_TEN, F_AS, F_EN]
        text = """|HP:\t{}\t|Mana:\t{}\t|
                \r|AD:\t{}\t|MD:\t{}\t|
                \r|Def:\t{}\t|MR:\t{}\t|
                \r|MS:\t{}\t|\t\t|
                \r|Reg:\t{}\t|Mreg:\t{}\t|
                \r|CD:\t{}\t|Crit:\t{}\t|
                \r|Gouge:\t{}\t|Pen:\t{}\t|
                \r|STA:\t{}\t|LS:\t{}\t|TEN:\t{}\t|AS:\t{}\t|ENC:\t{}"""
        print (text.format(F_HP, F_Mana, F_AD, F_MD, F_Def, F_MR, F_MS,
                            F_Reg, F_MReg, F_CD, F_Crit, F_Gouge, F_Pen,
                              F_STA, F_LS, F_TEN, F_AS, F_EN))
        print("--" * 25)

            


    
