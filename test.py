from rootNbo import nbo
from lib.parseNboSum import *
from lib.parseNBO import*
from lib.parseCMO import *
from lib.basicReadingFunctions import *
from lib.parsePert import*
from lib.parseNLMO import*
import pandas as pd
import numpy as np

singlet = "CN01_NN13_S_nbo.log"
triplet = "CuII_NBO7_Br.log"

#table = nbo(singlet)
#cmo = table.cmo
#nboSum = table.nboSum
table = nbo(triplet)
#cmoAlpha = table.cmoA
#cmoBeta = table.cmoB
nboSumAlpha = table.nboSumAlpha
nboSumBeta = table.nboSumBeta
#nboPertA = table.pertAlpha
#nboNlmoA = table.nlmoAlpha

tabCRFA,tabLPFA,tabLVFA,tabBDFA,tabBDSFA,tab3CFA,tab3CnFA,tab3CsFA = parseNboSum(nboSumAlpha)
tabCRFB,tabLPFB,tabLVFB,tabBDFB,tabBDSFB,tab3CFB,tab3CnFB,tab3CsFB = parseNboSum(nboSumBeta)
#tabCRF,tabBDF,tabBDSF,tab3CF,tab3CnF,tab3CsF = parseNBO(nboSum)  
#nboA = parseNBO(nboAlpha)
#tableNBOA = pd.DataFrame(nboA)

#pertA = parsePert(nboPertA)

#nboNLMOA = parseNLMO(nboNlmoA)
print(tabLPFA)
print(tabLPFB)