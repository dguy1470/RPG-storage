from RPG_stats import Stats

class statgrowth:
    #HP_growth,Mana_growth,Reg_growth,MReg_growth,AD_growth,AP_growth,MS_growth,Def_growth,MR_growth,CD_growth,Crit_growth,Gou_growth,Pen_growth,STA_growth,LS_growth,Ten_growth,AS_growth,Enc_growth

    def __init__(self,HP_growth,Mana_growth,AD_growth,MD_growth,Def_growth,MR_growth,MS_growth,Reg_growth,MReg_growth,
                    CD_growth,Crit_growth,Gou_growth,Pen_growth,STA_growth,LS_growth,Ten_growth,AS_growth,Enc_growth):

        self.HP_growth = HP_growth
        self.Mana_growth = Mana_growth
        
        self.AD_growth = AD_growth
        self.MD_growth = MD_growth

        self.Def_growth = Def_growth
        self.MR_growth = MR_growth
        self.MS_growth = MS_growth

        self.Reg_growth = Reg_growth
        self.MReg_growth = MReg_growth

        self.CD_growth = CD_growth
        self.Crit_growth = Crit_growth
        self.Gou_growth = Gou_growth
        self.Pen_growth = Pen_growth
        
        self.STA_growth = STA_growth
        self.LS_growth = LS_growth
        self.Ten_growth = Ten_growth
        self.AS_growth = AS_growth
        self.Enc_growth = Enc_growth

       

