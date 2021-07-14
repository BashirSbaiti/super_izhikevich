import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = "Intrinsically Bursting"
        self.C = 50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        self.stimVal = stimVal

myCell = cCell(stimVal=4000)
myCell.simulate()
if __name__=='__main__':
    izh.plotMyData(myCell)