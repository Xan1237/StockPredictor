import csv
import pandas as pd

# Read the CSV file
eth_data = pd.read_csv("ETH-CAD.csv")

# View the first 5 rows
#stock predictor
def gradient_descent1(tr1X, tr1Y,tr2X, tr2Y,tr3X, tr3Y,tr4X, tr4Y,tr5X, tr5Y, step):
    w0 = 0
    w1 =0
    pred = w1*tr1X + w0
    Loss = tr1Y - pred
    dw0 = -Loss
    dw1 = -Loss*tr1X
    w0 = w0 - step*(dw0)
    w1 = w1 - step*(dw1)
    print(w0)
    print(w1)
    pred = w1*tr2X + w0
    Loss = tr2Y - pred
    dw0 = -Loss
    dw1 = -Loss*tr2X
    w0 = w0 - step*(dw0)
    w1 = w1 - step*(dw1)
    print(w0)
    print(w1)
def training_set(w0,w1,tr1X, tr1Y, step):
    pred = w1*tr1X + w0
    Loss = tr1Y - pred
    dw0 = -Loss
    dw1 = -Loss*tr1X
    w0 = w0 - step*(dw0)
    w1 = w1 - step*(dw1)
    return w0,w1,Loss
step = 0.000000001
counter = 0
loup = False
lossed = False
## 0.01438619950004162 0.9989898165994946
while counter < 10:
    if loup == False:
        tr1=training_set(0,0,eth_data.loc[0].at["Open"],eth_data.loc[0].at["Close"],step)
    else:
        tr1=training_set(tr299[0],tr299[1],eth_data.loc[0].at["Open"],eth_data.loc[0].at["Close"],step)
    tr2=training_set(tr1[0],tr1[1],eth_data.loc[1].at["Open"],eth_data.loc[1].at["Close"],step)
    tr3=training_set(tr2[0],tr2[1],eth_data.loc[2].at["Open"],eth_data.loc[2].at["Close"],step)
    tr4=training_set(tr3[0],tr3[1],eth_data.loc[3].at["Open"],eth_data.loc[3].at["Close"],step)
    tr5=training_set(tr4[0],tr4[1],eth_data.loc[4].at["Open"],eth_data.loc[4].at["Close"],step)
    tr6=training_set(tr5[0],tr5[1],eth_data.loc[5].at["Open"],eth_data.loc[5].at["Close"],step)
    tr7=training_set(tr6[0],tr6[1],eth_data.loc[6].at["Open"],eth_data.loc[6].at["Close"],step)
    tr8=training_set(tr7[0],tr7[1],eth_data.loc[7].at["Open"],eth_data.loc[7].at["Close"],step)
    tr9=training_set(tr8[0],tr8[1],eth_data.loc[8].at["Open"],eth_data.loc[8].at["Close"],step)
    tr10=training_set(tr9[0],tr9[1],eth_data.loc[9].at["Open"],eth_data.loc[9].at["Close"],step)
    tr11=training_set(tr10[0],tr10[1],eth_data.loc[10].at["Open"],eth_data.loc[10].at["Close"],step)
    tr12=training_set(tr11[0],tr11[1],eth_data.loc[11].at["Open"],eth_data.loc[11].at["Close"],step)
    tr13=training_set(tr12[0],tr12[1],eth_data.loc[12].at["Open"],eth_data.loc[12].at["Close"],step)
    tr14=training_set(tr13[0],tr13[1],eth_data.loc[13].at["Open"],eth_data.loc[13].at["Close"],step)
    tr15=training_set(tr14[0],tr14[1],eth_data.loc[14].at["Open"],eth_data.loc[14].at["Close"],step)
    tr16=training_set(tr15[0],tr15[1],eth_data.loc[15].at["Open"],eth_data.loc[15].at["Close"],step)
    tr17=training_set(tr16[0],tr16[1],eth_data.loc[16].at["Open"],eth_data.loc[16].at["Close"],step)
    tr18=training_set(tr17[0],tr17[1],eth_data.loc[17].at["Open"],eth_data.loc[17].at["Close"],step)
    tr19=training_set(tr18[0],tr18[1],eth_data.loc[18].at["Open"],eth_data.loc[18].at["Close"],step)
    tr20=training_set(tr19[0],tr19[1],eth_data.loc[19].at["Open"],eth_data.loc[19].at["Close"],step)
    tr21=training_set(tr20[0],tr20[1],eth_data.loc[20].at["Open"],eth_data.loc[20].at["Close"],step)
    tr22=training_set(tr21[0],tr21[1],eth_data.loc[21].at["Open"],eth_data.loc[21].at["Close"],step)
    tr23=training_set(tr22[0],tr22[1],eth_data.loc[22].at["Open"],eth_data.loc[22].at["Close"],step)
    tr24=training_set(tr23[0],tr23[1],eth_data.loc[23].at["Open"],eth_data.loc[23].at["Close"],step)
    tr25=training_set(tr24[0],tr24[1],eth_data.loc[24].at["Open"],eth_data.loc[24].at["Close"],step)
    tr26=training_set(tr25[0],tr25[1],eth_data.loc[25].at["Open"],eth_data.loc[25].at["Close"],step)
    tr27=training_set(tr26[0],tr26[1],eth_data.loc[26].at["Open"],eth_data.loc[26].at["Close"],step)
    tr28=training_set(tr27[0],tr27[1],eth_data.loc[27].at["Open"],eth_data.loc[27].at["Close"],step)
    tr29=training_set(tr28[0],tr28[1],eth_data.loc[28].at["Open"],eth_data.loc[28].at["Close"],step)
    tr30=training_set(tr29[0],tr29[1],eth_data.loc[29].at["Open"],eth_data.loc[29].at["Close"],step)
    tr31=training_set(tr30[0],tr30[1],eth_data.loc[30].at["Open"],eth_data.loc[30].at["Close"],step)
    tr32=training_set(tr31[0],tr31[1],eth_data.loc[31].at["Open"],eth_data.loc[31].at["Close"],step)
    tr33=training_set(tr32[0],tr32[1],eth_data.loc[32].at["Open"],eth_data.loc[32].at["Close"],step)
    tr34=training_set(tr33[0],tr33[1],eth_data.loc[33].at["Open"],eth_data.loc[33].at["Close"],step)
    tr35=training_set(tr34[0],tr34[1],eth_data.loc[34].at["Open"],eth_data.loc[34].at["Close"],step)
    tr36=training_set(tr35[0],tr35[1],eth_data.loc[35].at["Open"],eth_data.loc[35].at["Close"],step)
    tr37=training_set(tr36[0],tr36[1],eth_data.loc[36].at["Open"],eth_data.loc[36].at["Close"],step)
    tr38=training_set(tr37[0],tr37[1],eth_data.loc[37].at["Open"],eth_data.loc[37].at["Close"],step)
    tr39=training_set(tr38[0],tr38[1],eth_data.loc[38].at["Open"],eth_data.loc[38].at["Close"],step)
    tr40=training_set(tr39[0],tr39[1],eth_data.loc[39].at["Open"],eth_data.loc[39].at["Close"],step)
    tr41=training_set(tr40[0],tr40[1],eth_data.loc[40].at["Open"],eth_data.loc[40].at["Close"],step)
    tr42=training_set(tr41[0],tr41[1],eth_data.loc[41].at["Open"],eth_data.loc[41].at["Close"],step)
    tr43=training_set(tr42[0],tr42[1],eth_data.loc[42].at["Open"],eth_data.loc[42].at["Close"],step)
    tr44=training_set(tr43[0],tr43[1],eth_data.loc[43].at["Open"],eth_data.loc[43].at["Close"],step)
    tr45=training_set(tr44[0],tr44[1],eth_data.loc[44].at["Open"],eth_data.loc[44].at["Close"],step)
    tr46=training_set(tr45[0],tr45[1],eth_data.loc[45].at["Open"],eth_data.loc[45].at["Close"],step)
    tr47=training_set(tr46[0],tr46[1],eth_data.loc[46].at["Open"],eth_data.loc[46].at["Close"],step)
    tr48=training_set(tr47[0],tr47[1],eth_data.loc[47].at["Open"],eth_data.loc[47].at["Close"],step)
    tr49=training_set(tr48[0],tr48[1],eth_data.loc[48].at["Open"],eth_data.loc[48].at["Close"],step)
    tr50=training_set(tr49[0],tr49[1],eth_data.loc[49].at["Open"],eth_data.loc[49].at["Close"],step)
    tr51=training_set(tr50[0],tr50[1],eth_data.loc[50].at["Open"],eth_data.loc[50].at["Close"],step)
    tr52=training_set(tr51[0],tr51[1],eth_data.loc[51].at["Open"],eth_data.loc[51].at["Close"],step)
    tr53=training_set(tr52[0],tr52[1],eth_data.loc[52].at["Open"],eth_data.loc[52].at["Close"],step)
    tr54=training_set(tr53[0],tr53[1],eth_data.loc[53].at["Open"],eth_data.loc[53].at["Close"],step)
    tr55=training_set(tr54[0],tr54[1],eth_data.loc[54].at["Open"],eth_data.loc[54].at["Close"],step)
    tr56=training_set(tr55[0],tr55[1],eth_data.loc[55].at["Open"],eth_data.loc[55].at["Close"],step)
    tr57=training_set(tr56[0],tr56[1],eth_data.loc[56].at["Open"],eth_data.loc[56].at["Close"],step)
    tr58=training_set(tr57[0],tr57[1],eth_data.loc[57].at["Open"],eth_data.loc[57].at["Close"],step)
    tr59=training_set(tr58[0],tr58[1],eth_data.loc[58].at["Open"],eth_data.loc[58].at["Close"],step)
    tr60=training_set(tr59[0],tr59[1],eth_data.loc[59].at["Open"],eth_data.loc[59].at["Close"],step)
    tr61=training_set(tr60[0],tr60[1],eth_data.loc[60].at["Open"],eth_data.loc[60].at["Close"],step)
    tr62=training_set(tr61[0],tr61[1],eth_data.loc[61].at["Open"],eth_data.loc[61].at["Close"],step)
    tr63=training_set(tr62[0],tr62[1],eth_data.loc[62].at["Open"],eth_data.loc[62].at["Close"],step)
    tr64=training_set(tr63[0],tr63[1],eth_data.loc[63].at["Open"],eth_data.loc[63].at["Close"],step)
    tr65=training_set(tr64[0],tr64[1],eth_data.loc[64].at["Open"],eth_data.loc[64].at["Close"],step)
    tr66=training_set(tr65[0],tr65[1],eth_data.loc[65].at["Open"],eth_data.loc[65].at["Close"],step)
    tr67=training_set(tr66[0],tr66[1],eth_data.loc[66].at["Open"],eth_data.loc[66].at["Close"],step)
    tr68=training_set(tr67[0],tr67[1],eth_data.loc[67].at["Open"],eth_data.loc[67].at["Close"],step)
    tr69=training_set(tr68[0],tr68[1],eth_data.loc[68].at["Open"],eth_data.loc[68].at["Close"],step)
    tr70=training_set(tr69[0],tr69[1],eth_data.loc[69].at["Open"],eth_data.loc[69].at["Close"],step)
    tr71=training_set(tr70[0],tr70[1],eth_data.loc[70].at["Open"],eth_data.loc[70].at["Close"],step)
    tr72=training_set(tr71[0],tr71[1],eth_data.loc[71].at["Open"],eth_data.loc[71].at["Close"],step)
    tr73=training_set(tr72[0],tr72[1],eth_data.loc[72].at["Open"],eth_data.loc[72].at["Close"],step)
    tr74=training_set(tr73[0],tr73[1],eth_data.loc[73].at["Open"],eth_data.loc[73].at["Close"],step)
    tr75=training_set(tr74[0],tr74[1],eth_data.loc[74].at["Open"],eth_data.loc[74].at["Close"],step)
    tr76=training_set(tr75[0],tr75[1],eth_data.loc[75].at["Open"],eth_data.loc[75].at["Close"],step)
    tr77=training_set(tr76[0],tr76[1],eth_data.loc[76].at["Open"],eth_data.loc[76].at["Close"],step)
    tr78=training_set(tr77[0],tr77[1],eth_data.loc[77].at["Open"],eth_data.loc[77].at["Close"],step)
    tr79=training_set(tr78[0],tr78[1],eth_data.loc[78].at["Open"],eth_data.loc[78].at["Close"],step)
    tr80=training_set(tr79[0],tr79[1],eth_data.loc[79].at["Open"],eth_data.loc[79].at["Close"],step)
    tr81=training_set(tr80[0],tr80[1],eth_data.loc[80].at["Open"],eth_data.loc[80].at["Close"],step)
    tr82=training_set(tr81[0],tr81[1],eth_data.loc[81].at["Open"],eth_data.loc[81].at["Close"],step)
    tr83=training_set(tr82[0],tr82[1],eth_data.loc[82].at["Open"],eth_data.loc[82].at["Close"],step)
    tr84=training_set(tr83[0],tr83[1],eth_data.loc[83].at["Open"],eth_data.loc[83].at["Close"],step)
    tr85=training_set(tr84[0],tr84[1],eth_data.loc[84].at["Open"],eth_data.loc[84].at["Close"],step)
    tr86=training_set(tr85[0],tr85[1],eth_data.loc[85].at["Open"],eth_data.loc[85].at["Close"],step)
    tr87=training_set(tr86[0],tr86[1],eth_data.loc[86].at["Open"],eth_data.loc[86].at["Close"],step)
    tr88=training_set(tr87[0],tr87[1],eth_data.loc[87].at["Open"],eth_data.loc[87].at["Close"],step)
    tr89=training_set(tr88[0],tr88[1],eth_data.loc[88].at["Open"],eth_data.loc[88].at["Close"],step)
    tr90=training_set(tr89[0],tr89[1],eth_data.loc[89].at["Open"],eth_data.loc[89].at["Close"],step)
    tr91=training_set(tr80[0],tr90[1],eth_data.loc[90].at["Open"],eth_data.loc[90].at["Close"],step)
    tr92=training_set(tr91[0],tr91[1],eth_data.loc[91].at["Open"],eth_data.loc[91].at["Close"],step)
    tr93=training_set(tr92[0],tr92[1],eth_data.loc[92].at["Open"],eth_data.loc[92].at["Close"],step)
    tr94=training_set(tr93[0],tr93[1],eth_data.loc[93].at["Open"],eth_data.loc[93].at["Close"],step)
    tr95=training_set(tr94[0],tr94[1],eth_data.loc[94].at["Open"],eth_data.loc[94].at["Close"],step)
    tr96=training_set(tr95[0],tr95[1],eth_data.loc[95].at["Open"],eth_data.loc[95].at["Close"],step)
    tr97=training_set(tr96[0],tr96[1],eth_data.loc[96].at["Open"],eth_data.loc[96].at["Close"],step)
    tr98=training_set(tr97[0],tr97[1],eth_data.loc[97].at["Open"],eth_data.loc[97].at["Close"],step)
    tr99=training_set(tr98[0],tr98[1],eth_data.loc[98].at["Open"],eth_data.loc[98].at["Close"],step)
    tr100=training_set(tr99[0],tr99[1],eth_data.loc[99].at["Open"],eth_data.loc[99].at["Close"],step)
    tr101=training_set(tr100[0],tr100[1],eth_data.loc[100].at["Open"],eth_data.loc[100].at["Close"],step)
    tr102=training_set(tr101[0],tr101[1],eth_data.loc[101].at["Open"],eth_data.loc[101].at["Close"],step)
    tr103=training_set(tr102[0],tr102[1],eth_data.loc[102].at["Open"],eth_data.loc[102].at["Close"],step)
    tr104=training_set(tr103[0],tr103[1],eth_data.loc[103].at["Open"],eth_data.loc[103].at["Close"],step)
    tr105=training_set(tr104[0],tr104[1],eth_data.loc[104].at["Open"],eth_data.loc[104].at["Close"],step)
    tr106=training_set(tr105[0],tr105[1],eth_data.loc[105].at["Open"],eth_data.loc[105].at["Close"],step)
    tr107=training_set(tr106[0],tr106[1],eth_data.loc[106].at["Open"],eth_data.loc[106].at["Close"],step)
    tr108=training_set(tr107[0],tr107[1],eth_data.loc[107].at["Open"],eth_data.loc[107].at["Close"],step)
    tr109=training_set(tr108[0],tr108[1],eth_data.loc[108].at["Open"],eth_data.loc[108].at["Close"],step)
    tr110=training_set(tr109[0],tr109[1],eth_data.loc[109].at["Open"],eth_data.loc[109].at["Close"],step)
    tr111=training_set(tr110[0],tr10[1],eth_data.loc[110].at["Open"],eth_data.loc[110].at["Close"],step)
    tr112=training_set(tr111[0],tr111[1],eth_data.loc[111].at["Open"],eth_data.loc[111].at["Close"],step)
    tr113=training_set(tr112[0],tr112[1],eth_data.loc[112].at["Open"],eth_data.loc[112].at["Close"],step)
    tr114=training_set(tr113[0],tr113[1],eth_data.loc[113].at["Open"],eth_data.loc[113].at["Close"],step)
    tr115=training_set(tr114[0],tr114[1],eth_data.loc[114].at["Open"],eth_data.loc[114].at["Close"],step)
    tr116=training_set(tr115[0],tr115[1],eth_data.loc[115].at["Open"],eth_data.loc[115].at["Close"],step)
    tr117=training_set(tr116[0],tr116[1],eth_data.loc[116].at["Open"],eth_data.loc[116].at["Close"],step)
    tr118=training_set(tr117[0],tr117[1],eth_data.loc[117].at["Open"],eth_data.loc[117].at["Close"],step)
    tr119=training_set(tr118[0],tr118[1],eth_data.loc[118].at["Open"],eth_data.loc[118].at["Close"],step)
    tr120=training_set(tr119[0],tr119[1],eth_data.loc[119].at["Open"],eth_data.loc[119].at["Close"],step)
    tr121=training_set(tr120[0],tr120[1],eth_data.loc[120].at["Open"],eth_data.loc[120].at["Close"],step)
    tr122=training_set(tr121[0],tr121[1],eth_data.loc[121].at["Open"],eth_data.loc[121].at["Close"],step)
    tr123=training_set(tr122[0],tr122[1],eth_data.loc[122].at["Open"],eth_data.loc[122].at["Close"],step)
    tr124=training_set(tr123[0],tr123[1],eth_data.loc[123].at["Open"],eth_data.loc[123].at["Close"],step)
    tr125=training_set(tr124[0],tr124[1],eth_data.loc[124].at["Open"],eth_data.loc[124].at["Close"],step)
    tr126=training_set(tr125[0],tr125[1],eth_data.loc[125].at["Open"],eth_data.loc[125].at["Close"],step)
    tr127=training_set(tr126[0],tr126[1],eth_data.loc[126].at["Open"],eth_data.loc[126].at["Close"],step)
    tr128=training_set(tr127[0],tr127[1],eth_data.loc[127].at["Open"],eth_data.loc[127].at["Close"],step)
    tr129=training_set(tr128[0],tr128[1],eth_data.loc[128].at["Open"],eth_data.loc[128].at["Close"],step)
    tr130=training_set(tr129[0],tr129[1],eth_data.loc[129].at["Open"],eth_data.loc[129].at["Close"],step)
    tr131=training_set(tr130[0],tr130[1],eth_data.loc[130].at["Open"],eth_data.loc[130].at["Close"],step)
    tr132=training_set(tr131[0],tr131[1],eth_data.loc[131].at["Open"],eth_data.loc[131].at["Close"],step)
    tr133=training_set(tr132[0],tr132[1],eth_data.loc[132].at["Open"],eth_data.loc[132].at["Close"],step)
    tr134=training_set(tr133[0],tr133[1],eth_data.loc[133].at["Open"],eth_data.loc[133].at["Close"],step)
    tr135=training_set(tr134[0],tr134[1],eth_data.loc[134].at["Open"],eth_data.loc[134].at["Close"],step)
    tr136=training_set(tr135[0],tr135[1],eth_data.loc[135].at["Open"],eth_data.loc[135].at["Close"],step)
    tr137=training_set(tr136[0],tr136[1],eth_data.loc[136].at["Open"],eth_data.loc[136].at["Close"],step)
    tr138=training_set(tr137[0],tr137[1],eth_data.loc[137].at["Open"],eth_data.loc[137].at["Close"],step)
    tr139=training_set(tr138[0],tr138[1],eth_data.loc[138].at["Open"],eth_data.loc[138].at["Close"],step)
    tr140=training_set(tr139[0],tr139[1],eth_data.loc[139].at["Open"],eth_data.loc[139].at["Close"],step)
    tr141=training_set(tr140[0],tr140[1],eth_data.loc[140].at["Open"],eth_data.loc[140].at["Close"],step)
    tr142=training_set(tr141[0],tr141[1],eth_data.loc[141].at["Open"],eth_data.loc[141].at["Close"],step)
    tr143=training_set(tr142[0],tr142[1],eth_data.loc[142].at["Open"],eth_data.loc[142].at["Close"],step)
    tr144=training_set(tr143[0],tr143[1],eth_data.loc[143].at["Open"],eth_data.loc[143].at["Close"],step)
    tr145=training_set(tr144[0],tr144[1],eth_data.loc[144].at["Open"],eth_data.loc[144].at["Close"],step)
    tr146=training_set(tr145[0],tr145[1],eth_data.loc[145].at["Open"],eth_data.loc[145].at["Close"],step)
    tr147=training_set(tr146[0],tr146[1],eth_data.loc[146].at["Open"],eth_data.loc[146].at["Close"],step)
    tr148=training_set(tr147[0],tr147[1],eth_data.loc[147].at["Open"],eth_data.loc[147].at["Close"],step)
    tr149=training_set(tr148[0],tr148[1],eth_data.loc[148].at["Open"],eth_data.loc[148].at["Close"],step)
    tr150=training_set(tr149[0],tr149[1],eth_data.loc[149].at["Open"],eth_data.loc[149].at["Close"],step)
    tr151=training_set(tr150[0],tr150[1],eth_data.loc[150].at["Open"],eth_data.loc[150].at["Close"],step)
    tr152=training_set(tr151[0],tr151[1],eth_data.loc[151].at["Open"],eth_data.loc[151].at["Close"],step)
    tr153=training_set(tr152[0],tr152[1],eth_data.loc[152].at["Open"],eth_data.loc[152].at["Close"],step)
    tr154=training_set(tr153[0],tr153[1],eth_data.loc[153].at["Open"],eth_data.loc[153].at["Close"],step)
    tr155=training_set(tr154[0],tr154[1],eth_data.loc[154].at["Open"],eth_data.loc[154].at["Close"],step)
    tr156=training_set(tr155[0],tr155[1],eth_data.loc[155].at["Open"],eth_data.loc[155].at["Close"],step)
    tr157=training_set(tr156[0],tr156[1],eth_data.loc[156].at["Open"],eth_data.loc[156].at["Close"],step)
    tr158=training_set(tr157[0],tr157[1],eth_data.loc[157].at["Open"],eth_data.loc[157].at["Close"],step)
    tr159=training_set(tr158[0],tr158[1],eth_data.loc[158].at["Open"],eth_data.loc[158].at["Close"],step)
    tr160=training_set(tr159[0],tr159[1],eth_data.loc[159].at["Open"],eth_data.loc[159].at["Close"],step)
    tr161=training_set(tr160[0],tr160[1],eth_data.loc[160].at["Open"],eth_data.loc[160].at["Close"],step)
    tr162=training_set(tr161[0],tr161[1],eth_data.loc[161].at["Open"],eth_data.loc[161].at["Close"],step)
    tr163=training_set(tr162[0],tr162[1],eth_data.loc[162].at["Open"],eth_data.loc[162].at["Close"],step)
    tr164=training_set(tr163[0],tr163[1],eth_data.loc[163].at["Open"],eth_data.loc[163].at["Close"],step)
    tr165=training_set(tr164[0],tr164[1],eth_data.loc[164].at["Open"],eth_data.loc[164].at["Close"],step)
    tr166=training_set(tr165[0],tr165[1],eth_data.loc[165].at["Open"],eth_data.loc[165].at["Close"],step)
    tr167=training_set(tr166[0],tr166[1],eth_data.loc[166].at["Open"],eth_data.loc[166].at["Close"],step)
    tr168=training_set(tr167[0],tr167[1],eth_data.loc[167].at["Open"],eth_data.loc[167].at["Close"],step)
    tr169=training_set(tr168[0],tr168[1],eth_data.loc[168].at["Open"],eth_data.loc[168].at["Close"],step)
    tr170=training_set(tr169[0],tr169[1],eth_data.loc[169].at["Open"],eth_data.loc[169].at["Close"],step)
    tr171=training_set(tr170[0],tr170[1],eth_data.loc[170].at["Open"],eth_data.loc[170].at["Close"],step)
    tr172=training_set(tr171[0],tr171[1],eth_data.loc[171].at["Open"],eth_data.loc[171].at["Close"],step)
    tr173=training_set(tr172[0],tr172[1],eth_data.loc[172].at["Open"],eth_data.loc[172].at["Close"],step)
    tr174=training_set(tr173[0],tr173[1],eth_data.loc[173].at["Open"],eth_data.loc[173].at["Close"],step)
    tr175=training_set(tr174[0],tr174[1],eth_data.loc[174].at["Open"],eth_data.loc[174].at["Close"],step)
    tr176=training_set(tr175[0],tr175[1],eth_data.loc[175].at["Open"],eth_data.loc[175].at["Close"],step)
    tr177=training_set(tr176[0],tr176[1],eth_data.loc[176].at["Open"],eth_data.loc[176].at["Close"],step)
    tr178=training_set(tr177[0],tr177[1],eth_data.loc[177].at["Open"],eth_data.loc[177].at["Close"],step)
    tr179=training_set(tr178[0],tr178[1],eth_data.loc[178].at["Open"],eth_data.loc[178].at["Close"],step)
    tr180=training_set(tr179[0],tr179[1],eth_data.loc[179].at["Open"],eth_data.loc[179].at["Close"],step)
    tr181=training_set(tr180[0],tr180[1],eth_data.loc[180].at["Open"],eth_data.loc[180].at["Close"],step)
    tr182=training_set(tr181[0],tr181[1],eth_data.loc[181].at["Open"],eth_data.loc[181].at["Close"],step)
    tr183=training_set(tr182[0],tr182[1],eth_data.loc[182].at["Open"],eth_data.loc[182].at["Close"],step)
    tr184=training_set(tr183[0],tr183[1],eth_data.loc[183].at["Open"],eth_data.loc[183].at["Close"],step)
    tr185=training_set(tr184[0],tr184[1],eth_data.loc[184].at["Open"],eth_data.loc[184].at["Close"],step)
    tr186=training_set(tr185[0],tr185[1],eth_data.loc[185].at["Open"],eth_data.loc[185].at["Close"],step)
    tr187=training_set(tr186[0],tr186[1],eth_data.loc[186].at["Open"],eth_data.loc[186].at["Close"],step)
    tr188=training_set(tr187[0],tr187[1],eth_data.loc[187].at["Open"],eth_data.loc[187].at["Close"],step)
    tr189=training_set(tr188[0],tr188[1],eth_data.loc[188].at["Open"],eth_data.loc[188].at["Close"],step)
    tr190=training_set(tr189[0],tr189[1],eth_data.loc[189].at["Open"],eth_data.loc[189].at["Close"],step)
    tr191=training_set(tr190[0],tr190[1],eth_data.loc[190].at["Open"],eth_data.loc[190].at["Close"],step)
    tr192=training_set(tr191[0],tr191[1],eth_data.loc[191].at["Open"],eth_data.loc[191].at["Close"],step)
    tr193=training_set(tr192[0],tr192[1],eth_data.loc[192].at["Open"],eth_data.loc[192].at["Close"],step)
    tr194=training_set(tr193[0],tr193[1],eth_data.loc[193].at["Open"],eth_data.loc[193].at["Close"],step)
    tr195=training_set(tr194[0],tr194[1],eth_data.loc[194].at["Open"],eth_data.loc[194].at["Close"],step)
    tr196=training_set(tr195[0],tr195[1],eth_data.loc[195].at["Open"],eth_data.loc[195].at["Close"],step)
    tr197=training_set(tr196[0],tr196[1],eth_data.loc[196].at["Open"],eth_data.loc[196].at["Close"],step)
    tr198=training_set(tr197[0],tr197[1],eth_data.loc[197].at["Open"],eth_data.loc[197].at["Close"],step)
    tr199=training_set(tr198[0],tr198[1],eth_data.loc[198].at["Open"],eth_data.loc[198].at["Close"],step)
    tr200=training_set(tr199[0],tr199[1],eth_data.loc[199].at["Open"],eth_data.loc[199].at["Close"],step)
    tr201=training_set(tr200[0],tr200[1],eth_data.loc[200].at["Open"],eth_data.loc[200].at["Close"],step)
    tr202=training_set(tr201[0],tr201[1],eth_data.loc[201].at["Open"],eth_data.loc[201].at["Close"],step)
    tr203=training_set(tr202[0],tr202[1],eth_data.loc[202].at["Open"],eth_data.loc[202].at["Close"],step)
    tr204=training_set(tr203[0],tr203[1],eth_data.loc[203].at["Open"],eth_data.loc[203].at["Close"],step)
    tr205=training_set(tr204[0],tr204[1],eth_data.loc[204].at["Open"],eth_data.loc[204].at["Close"],step)
    tr206=training_set(tr205[0],tr205[1],eth_data.loc[205].at["Open"],eth_data.loc[205].at["Close"],step)
    tr207=training_set(tr206[0],tr206[1],eth_data.loc[206].at["Open"],eth_data.loc[206].at["Close"],step)
    tr208=training_set(tr207[0],tr207[1],eth_data.loc[207].at["Open"],eth_data.loc[207].at["Close"],step)
    tr209=training_set(tr208[0],tr208[1],eth_data.loc[208].at["Open"],eth_data.loc[208].at["Close"],step)
    tr210=training_set(tr209[0],tr209[1],eth_data.loc[209].at["Open"],eth_data.loc[209].at["Close"],step)
    tr211=training_set(tr210[0],tr210[1],eth_data.loc[210].at["Open"],eth_data.loc[210].at["Close"],step)
    tr212=training_set(tr211[0],tr211[1],eth_data.loc[211].at["Open"],eth_data.loc[211].at["Close"],step)
    tr213=training_set(tr212[0],tr212[1],eth_data.loc[212].at["Open"],eth_data.loc[212].at["Close"],step)
    tr214=training_set(tr213[0],tr213[1],eth_data.loc[213].at["Open"],eth_data.loc[213].at["Close"],step)
    tr215=training_set(tr214[0],tr214[1],eth_data.loc[214].at["Open"],eth_data.loc[214].at["Close"],step)
    tr216=training_set(tr215[0],tr215[1],eth_data.loc[215].at["Open"],eth_data.loc[215].at["Close"],step)
    tr217=training_set(tr216[0],tr216[1],eth_data.loc[216].at["Open"],eth_data.loc[216].at["Close"],step)
    tr218=training_set(tr217[0],tr217[1],eth_data.loc[217].at["Open"],eth_data.loc[217].at["Close"],step)
    tr219=training_set(tr218[0],tr218[1],eth_data.loc[218].at["Open"],eth_data.loc[218].at["Close"],step)
    tr220=training_set(tr219[0],tr219[1],eth_data.loc[219].at["Open"],eth_data.loc[219].at["Close"],step)
    tr221=training_set(tr220[0],tr220[1],eth_data.loc[220].at["Open"],eth_data.loc[220].at["Close"],step)
    tr222=training_set(tr221[0],tr221[1],eth_data.loc[221].at["Open"],eth_data.loc[221].at["Close"],step)
    tr223=training_set(tr222[0],tr222[1],eth_data.loc[222].at["Open"],eth_data.loc[222].at["Close"],step)
    tr224=training_set(tr223[0],tr223[1],eth_data.loc[223].at["Open"],eth_data.loc[223].at["Close"],step)
    tr225=training_set(tr224[0],tr224[1],eth_data.loc[224].at["Open"],eth_data.loc[224].at["Close"],step)
    tr226=training_set(tr225[0],tr225[1],eth_data.loc[225].at["Open"],eth_data.loc[225].at["Close"],step)
    tr227=training_set(tr226[0],tr226[1],eth_data.loc[226].at["Open"],eth_data.loc[226].at["Close"],step)
    tr228=training_set(tr227[0],tr227[1],eth_data.loc[227].at["Open"],eth_data.loc[227].at["Close"],step)
    tr229=training_set(tr228[0],tr228[1],eth_data.loc[228].at["Open"],eth_data.loc[228].at["Close"],step)
    tr230=training_set(tr229[0],tr229[1],eth_data.loc[229].at["Open"],eth_data.loc[229].at["Close"],step)
    tr231=training_set(tr230[0],tr230[1],eth_data.loc[230].at["Open"],eth_data.loc[230].at["Close"],step)
    tr232=training_set(tr231[0],tr231[1],eth_data.loc[231].at["Open"],eth_data.loc[231].at["Close"],step)
    tr233=training_set(tr232[0],tr232[1],eth_data.loc[232].at["Open"],eth_data.loc[232].at["Close"],step)
    tr234=training_set(tr233[0],tr233[1],eth_data.loc[233].at["Open"],eth_data.loc[233].at["Close"],step)
    tr235=training_set(tr234[0],tr234[1],eth_data.loc[234].at["Open"],eth_data.loc[234].at["Close"],step)
    tr236=training_set(tr235[0],tr235[1],eth_data.loc[235].at["Open"],eth_data.loc[235].at["Close"],step)
    tr237=training_set(tr236[0],tr236[1],eth_data.loc[236].at["Open"],eth_data.loc[236].at["Close"],step)
    tr238=training_set(tr237[0],tr237[1],eth_data.loc[237].at["Open"],eth_data.loc[237].at["Close"],step)
    tr239=training_set(tr238[0],tr238[1],eth_data.loc[238].at["Open"],eth_data.loc[238].at["Close"],step)
    tr240=training_set(tr239[0],tr239[1],eth_data.loc[239].at["Open"],eth_data.loc[239].at["Close"],step)
    tr241=training_set(tr240[0],tr240[1],eth_data.loc[240].at["Open"],eth_data.loc[240].at["Close"],step)
    tr242=training_set(tr241[0],tr241[1],eth_data.loc[241].at["Open"],eth_data.loc[241].at["Close"],step)
    tr243=training_set(tr242[0],tr242[1],eth_data.loc[242].at["Open"],eth_data.loc[242].at["Close"],step)
    tr244=training_set(tr243[0],tr243[1],eth_data.loc[243].at["Open"],eth_data.loc[243].at["Close"],step)
    tr245=training_set(tr244[0],tr244[1],eth_data.loc[244].at["Open"],eth_data.loc[244].at["Close"],step)
    tr246=training_set(tr245[0],tr245[1],eth_data.loc[245].at["Open"],eth_data.loc[245].at["Close"],step)
    tr247=training_set(tr246[0],tr246[1],eth_data.loc[246].at["Open"],eth_data.loc[246].at["Close"],step)
    tr248=training_set(tr247[0],tr247[1],eth_data.loc[247].at["Open"],eth_data.loc[247].at["Close"],step)
    tr249=training_set(tr248[0],tr248[1],eth_data.loc[248].at["Open"],eth_data.loc[248].at["Close"],step)
    tr250=training_set(tr249[0],tr249[1],eth_data.loc[249].at["Open"],eth_data.loc[249].at["Close"],step)
    tr251=training_set(tr250[0],tr250[1],eth_data.loc[250].at["Open"],eth_data.loc[250].at["Close"],step)
    tr252=training_set(tr251[0],tr251[1],eth_data.loc[251].at["Open"],eth_data.loc[251].at["Close"],step)
    tr253=training_set(tr252[0],tr252[1],eth_data.loc[252].at["Open"],eth_data.loc[252].at["Close"],step)
    tr254=training_set(tr253[0],tr253[1],eth_data.loc[253].at["Open"],eth_data.loc[253].at["Close"],step)
    tr255=training_set(tr254[0],tr254[1],eth_data.loc[254].at["Open"],eth_data.loc[254].at["Close"],step)
    tr256=training_set(tr255[0],tr255[1],eth_data.loc[255].at["Open"],eth_data.loc[255].at["Close"],step)
    tr257=training_set(tr256[0],tr256[1],eth_data.loc[256].at["Open"],eth_data.loc[256].at["Close"],step)
    tr258=training_set(tr257[0],tr257[1],eth_data.loc[257].at["Open"],eth_data.loc[257].at["Close"],step)
    tr259=training_set(tr258[0],tr258[1],eth_data.loc[258].at["Open"],eth_data.loc[258].at["Close"],step)
    tr260=training_set(tr259[0],tr259[1],eth_data.loc[259].at["Open"],eth_data.loc[259].at["Close"],step)
    tr261=training_set(tr260[0],tr260[1],eth_data.loc[260].at["Open"],eth_data.loc[260].at["Close"],step)
    tr262=training_set(tr261[0],tr261[1],eth_data.loc[261].at["Open"],eth_data.loc[261].at["Close"],step)
    tr263=training_set(tr262[0],tr262[1],eth_data.loc[262].at["Open"],eth_data.loc[262].at["Close"],step)
    tr264=training_set(tr263[0],tr263[1],eth_data.loc[263].at["Open"],eth_data.loc[263].at["Close"],step)
    tr265=training_set(tr264[0],tr264[1],eth_data.loc[264].at["Open"],eth_data.loc[264].at["Close"],step)
    tr266=training_set(tr265[0],tr265[1],eth_data.loc[265].at["Open"],eth_data.loc[265].at["Close"],step)
    tr267=training_set(tr266[0],tr266[1],eth_data.loc[266].at["Open"],eth_data.loc[266].at["Close"],step)
    tr268=training_set(tr267[0],tr267[1],eth_data.loc[267].at["Open"],eth_data.loc[267].at["Close"],step)
    tr269=training_set(tr268[0],tr268[1],eth_data.loc[268].at["Open"],eth_data.loc[268].at["Close"],step)
    tr270=training_set(tr269[0],tr269[1],eth_data.loc[269].at["Open"],eth_data.loc[269].at["Close"],step)
    tr271=training_set(tr270[0],tr270[1],eth_data.loc[270].at["Open"],eth_data.loc[270].at["Close"],step)
    tr272=training_set(tr271[0],tr271[1],eth_data.loc[271].at["Open"],eth_data.loc[271].at["Close"],step)
    tr273=training_set(tr272[0],tr272[1],eth_data.loc[272].at["Open"],eth_data.loc[272].at["Close"],step)
    tr274=training_set(tr273[0],tr273[1],eth_data.loc[273].at["Open"],eth_data.loc[273].at["Close"],step)
    tr275=training_set(tr274[0],tr274[1],eth_data.loc[274].at["Open"],eth_data.loc[274].at["Close"],step)
    tr276=training_set(tr275[0],tr275[1],eth_data.loc[275].at["Open"],eth_data.loc[275].at["Close"],step)
    tr277=training_set(tr276[0],tr276[1],eth_data.loc[276].at["Open"],eth_data.loc[276].at["Close"],step)
    tr278=training_set(tr277[0],tr277[1],eth_data.loc[277].at["Open"],eth_data.loc[277].at["Close"],step)
    tr279=training_set(tr278[0],tr278[1],eth_data.loc[278].at["Open"],eth_data.loc[278].at["Close"],step)
    tr280=training_set(tr279[0],tr279[1],eth_data.loc[279].at["Open"],eth_data.loc[279].at["Close"],step)
    tr281=training_set(tr280[0],tr280[1],eth_data.loc[280].at["Open"],eth_data.loc[280].at["Close"],step)
    tr282=training_set(tr281[0],tr281[1],eth_data.loc[281].at["Open"],eth_data.loc[281].at["Close"],step)
    tr283=training_set(tr282[0],tr282[1],eth_data.loc[282].at["Open"],eth_data.loc[282].at["Close"],step)
    tr284=training_set(tr283[0],tr283[1],eth_data.loc[283].at["Open"],eth_data.loc[283].at["Close"],step)
    tr285=training_set(tr284[0],tr284[1],eth_data.loc[284].at["Open"],eth_data.loc[284].at["Close"],step)
    tr286=training_set(tr285[0],tr285[1],eth_data.loc[285].at["Open"],eth_data.loc[285].at["Close"],step)
    tr287=training_set(tr286[0],tr286[1],eth_data.loc[286].at["Open"],eth_data.loc[286].at["Close"],step)
    tr288=training_set(tr287[0],tr287[1],eth_data.loc[287].at["Open"],eth_data.loc[287].at["Close"],step)
    tr289=training_set(tr288[0],tr288[1],eth_data.loc[288].at["Open"],eth_data.loc[288].at["Close"],step)
    tr290=training_set(tr289[0],tr289[1],eth_data.loc[289].at["Open"],eth_data.loc[289].at["Close"],step)
    tr291=training_set(tr280[0],tr290[1],eth_data.loc[290].at["Open"],eth_data.loc[290].at["Close"],step)
    tr292=training_set(tr291[0],tr291[1],eth_data.loc[291].at["Open"],eth_data.loc[291].at["Close"],step)
    tr293=training_set(tr292[0],tr292[1],eth_data.loc[292].at["Open"],eth_data.loc[292].at["Close"],step)
    tr294=training_set(tr293[0],tr293[1],eth_data.loc[293].at["Open"],eth_data.loc[293].at["Close"],step)
    tr295=training_set(tr294[0],tr294[1],eth_data.loc[294].at["Open"],eth_data.loc[294].at["Close"],step)
    tr296=training_set(tr295[0],tr295[1],eth_data.loc[295].at["Open"],eth_data.loc[295].at["Close"],step)
    tr297=training_set(tr296[0],tr296[1],eth_data.loc[296].at["Open"],eth_data.loc[296].at["Close"],step)
    tr298=training_set(tr297[0],tr297[1],eth_data.loc[297].at["Open"],eth_data.loc[297].at["Close"],step)
    tr299=training_set(tr298[0],tr298[1],eth_data.loc[298].at["Open"],eth_data.loc[298].at["Close"],step)
    counter += 1
    loup = True

#testing 
print(float(tr299[1]*eth_data.loc[250].at["Open"]+tr299[0]))
print(eth_data.loc[250].at["Close"])
print(float(tr299[0]))
print(float(tr299[1]))


