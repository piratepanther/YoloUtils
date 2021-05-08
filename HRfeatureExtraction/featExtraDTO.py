from  enum import Enum


class alertLevelCol(Enum):
    YELLOW = 'yellow'
    RED = 'red'
    BLUE = 'blue'

class alertLevelEmu(Enum):
    LEVEL1 = 100
    LEVEL2 = 200
    LEVEL3 = 300

class alertLevelParameter(Enum):
    signalEnergyPara = 1
    signalMaxPara = 1
    signalMeanPara = 1
    signalVarPara = 1
    signalProportionPara = 1
    vibrationDegreePara = 1


class feaExtra:

    signalEnergy = ''
    signalMax = ''
    signalMean = ''
    signalVar = ''
    signalProportion = ''
    vibrationDegree = ''
    alertLevelNum = ''


    alertLevel=''


    def __init__(self, signalEnergy,signalMax ,signalMean, signalVar, signalProportion, vibrationDegree,alertLevelNum):
        self.signalEnergy = signalEnergy
        self.signalMax = signalMax
        self.signalMean = signalMean
        self.signalVar = signalVar
        self.signalProportion = signalProportion
        self.vibrationDegree = vibrationDegree
        self.alertLevelNum = alertLevelNum
        self.alertLevel = self.getalertLevelCol(self.alertLevelNum)

    def getalertLevelCol(self,alertLevelNum):
        if alertLevelNum<=alertLevelEmu.LEVEL1.value:
            alertLevel= alertLevelCol.BLUE.value

        elif alertLevelNum <=alertLevelEmu.LEVEL2.value:
            alertLevel = alertLevelCol.YELLOW.value

        else:
            alertLevel = alertLevelCol.RED.value
        return alertLevel

    def displayfeaExtra(self):
        print("signalEnergy : ", self.signalEnergy,
              "signalMax : ", self.signalMax,
              "signalMean : ", self.signalMean,
              "signalVar : ", self.signalVar,
              "signalProportion : ", str(self.signalEnergy)+'%',
              "signalEnergy : ", str(self.signalEnergy)+'%',
              "alertLevelNum : ", self.alertLevelNum,
              "alertLevel : ", self.alertLevel
              )
