from RPG_stats import Stats

def statFileRead (fileName):
    f = open(fileName, "r")
    f.readline()
    global charClass
    charClass = [Stats(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,)]
    for x in f:
    
        name=x[:x.index("|")]
        x=x[x.index("|")+1:]
        name = name.strip()
        #print(name)

        HP=x[:x.index("|")]
        x=x[x.index("|")+1:]
        HP = HP.strip()
        #print(HP)

        Mana=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Mana = int(Mana.strip())
        #print(Mana)

        AD=x[:x.index("|")]
        x=x[x.index("|")+1:]
        AD = int(AD.strip())
        #print(AD)

        AP=x[:x.index("|")]
        x=x[x.index("|")+1:]
        AP = int(AP.strip())
        #print(AP)

        Def=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Def = int(Def.strip())
        #print(Def)

        MR=x[:x.index("|")]
        x=x[x.index("|")+1:]
        MR = int(MR.strip())
        #print(MR)

        MS=x[:x.index("|")]
        x=x[x.index("|")+1:]
        MS = int(MS.strip())
        #print(MS)

        Reg=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Reg = int(Reg.strip())
        #print(Reg)

        MReg=x[:x.index("|")]
        x=x[x.index("|")+1:]
        MReg = int(MReg.strip())
        #print(MReg)

        CD=x[:x.index("|")]
        x=x[x.index("|")+1:]
        CD = int(CD.strip())
        #print(CD)

        Crit=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Crit = int(Crit.strip())
        #print(Crit)

        Gouge=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Gouge = int(Gouge.strip())
        #print(Gouge)

        Pen=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Pen = int(Pen.strip())
        #print(Pen)

        STA=x[:x.index("|")]
        x=x[x.index("|")+1:]
        STA = int(STA.strip())
        #print(STA)

        LS=x[:x.index("|")]
        x=x[x.index("|")+1:]
        LS = int(LS.strip())
        #print(LS)

        Ten=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Ten = int(Ten.strip())
        #print(Ten)

        AS=x[:x.index("|")]
        x=x[x.index("|")+1:]
        AS = float(AS.strip())
        #print(AS)

        Enc=x[:x.index("|")]
        x=x[x.index("|")+1:]
        Enc = float(Enc.strip())
        #print(Enc)

        charClass.append(Stats(HP,Mana,AD,AP,Def,MR,MS,Reg,MReg,CD,Crit,Gouge,Pen,STA,LS,Ten,AS,Enc))


    f.close()
    del charClass[0]
    return charClass
