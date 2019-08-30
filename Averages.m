clc;
clear all;
fiveNoBN=[0.3040 0.3216 0.6328];
tenNoBN=[0.1735];
tenWBN=[0.5420, 0.0124];%outlier 1
tenWBN=tenWBN(1);
tenNoBN=[];
fifteenNoBN=[0.2685 0.5250 ];

twoFiveNoBN=[0.2442,0.3243];
twoFiveWBN=[0.3060,0.3119, 0.3326];
fourtyNoBN=[0.0468,0.3442,0.3392];
sixtyNoBN=[0.0187,0.3345,0.0807];
sixtyWBN=[0.5505,0.5019,0.4708];%Outlier
baseN=[0.1173,0.1122];
aveN=[mean(fiveNoBN) mean([tenNoBN tenWBN]) mean(fifteenNoBN)  mean([twoFiveNoBN twoFiveWBN]) mean(fourtyNoBN) mean([sixtyNoBN sixtyNoBN]) mean(baseN)];
fiveNoB1=[0.1437 0.1476 0.1880];
tenWB1=[0.1324,0.0417];
tenWB1(2)=[];
tenNoB1=[10.5655,11.1843]; %this one
tenNoB1=[];
fifteenNoB1=[0.0475 0.0468 0.0396];
fifteenNoB1(3)=[];
twoFiveNoB1=[0.0308,0.0267, 0.0400];
twoFiveNoB1(2)=[];
twoFiveWB1=[0.0231, 0.0186];
twoFiveWB1=[];
fourtyNoB1=[0.0321, 0.0360, 0.0235];
fourtyNoB1(3)=[];
sixtyNoB1=[0.0234, 0.0393];
sixtyWB1=[0.0235, 0.0249, 0.0191];
base1=[0.0416, 0.0305];%this one
base1(1)=[];
aveOne=[mean(fiveNoB1) mean([tenNoB1 tenWB1]) mean(fifteenNoB1)  mean([twoFiveNoB1 twoFiveWB1]) mean(fourtyNoB1) mean([sixtyNoB1 sixtyNoB1]) mean(base1)];

fiveNoB4=[0.2824 0.2083 0.2393];
tenWB4=[0.0750 0.0717];
tenWB4=[];
tenNoB4=[0.1395,0.1212];
fifteenNoB4=[0.1045 0.1361 0.1093];
twoFiveNoB4=[0.1097, 0.1091];
twoFiveWB4=[0.0433, 0.0942];
fourtyNoB4=[0.0877, 0.1040,0.1271];
sixtyNoB4=[0.1102];
sixtyWB4=[0.0778, 0.0820];
base4=[0.1019, 0.0862];
aveFour=[mean(fiveNoB4) mean([tenNoB4 tenWB4]) mean(fifteenNoB4)  mean([twoFiveNoB4 twoFiveWB4]) mean(fourtyNoB4) mean([sixtyNoB4 sixtyNoB4]) mean(base4)];

fiveNoB8=[0.1468 0.2737 0.1635];
tenNoB8=[0.0732, 0.0397];
tenNoB8=[];
tenWB8=[0.0705,0.1059];
tenWB8=tenWB8(2);
fifteenNoB8=[0.0797 0.0573 0.0307];
fifteenNoB8(2:3)=[];
twoFiveNoB8=[0.0707,0.0859];
twoFiveWB8=[0.0813, 0.0862];
fourtyNoB8=[0.0776,0.0516];
sixtyNoB8=[0.0918,0.0985];
sixtyWB8=[0.1062, 0.0826];
base8=[0.0593, 0.0731];
base8=base8(1);
aveEight=[mean(fiveNoB8) mean([tenNoB8 tenWB8]) mean(fifteenNoB8)  mean([twoFiveNoB8 twoFiveWB8]) mean(fourtyNoB8) mean([sixtyNoB8 sixtyNoB8]) mean(base8)];

aveAll=aveEight+aveFour+aveOne+aveN;
aveAll=aveAll/4

%Notes Two seems to be a strange batch throughout. Baseline at No FEC is
%weird. Might re run for more data BUt overall shows trend if two is
%excluded
fiveNoBDec1=[0.1146 0.1310 0.1479];
tenNoBDec1=[10.0587 10.7423];
tenNoBDec1=[];
tenWBDec1=[0.1422 0.0433];
tenWBDec1(2)=[];
fifteenNoBDec1=[0.0366 0.0289 0.0214];
twoFiveNoBDec1=[0.0181 0.0232];
twoFiveNoBDec1=[];
twoFiveWBDec1=[0.0290 0.0231 0.0310 0.0194];
fourtyNoBDec1=[0.0479, 0.0196 0.0192];
fourtyNoBDec1(1)=[];
sixtyNoBDec1=[0.0084 0.0178];
sixtyWBDec1=[0.0295 0.0294 0.0245];
sixtyWBDec1=[];
baseDec1=[0.0267, 0.0333];
aveDec1=[mean(fiveNoBDec1) mean([tenNoBDec1 tenWBDec1]) mean(fifteenNoBDec1) mean([twoFiveNoBDec1 twoFiveWBDec1]) mean([fourtyNoBDec1]) mean([sixtyNoBDec1 sixtyWBDec1]) mean([baseDec1])]

fiveNoBDec4=[0.2056 0.1326 0.1402];
tenNoBDec4=[0.0816 0.0652];
tenWBDec4=[0.0686, 0.0590];
tenNoBDec4(2)=[];
tenWBDec4=[];
fifteenNoBDec4=[0.0720 0.0958 0.0712];
twoFiveNoBDec4=[0.0717 0.0730  ];
twoFiveWBDec4=[0.0971 0.0461 0.3258];
twoFiveWBDec4(2:3)=[];
fourtyNoBDec4=[0.0718 0.0952 0.0904 ];
sixtyNoBDec4=[0.0866];
sixtyWBDec4=[0.0861 0.0888];
sixtyWBDec4(2)=[];
baseDec4=[0.0840 0.0717];
aveDec4=[mean(fiveNoBDec4) mean([tenNoBDec4 tenWBDec4]) mean(fifteenNoBDec4) mean([twoFiveNoBDec4 twoFiveWBDec4]) mean(fourtyNoBDec4) mean([sixtyNoBDec4 sixtyWBDec4]) mean([baseDec4])]

fiveNoBDec8=[0.0845 0.1935 0.0989];
tenNoBDec8=[0.0470 0.0602];
tenWBDec8=[0.0278, 0.0597];
tenWBDec8(1)=[];
tenNoBDec8(1)=[];
fifteenNoBDec8=[0.0477 0.0823 0.0250];%Note
fifteenNoBDec8=fifteenNoBDec8(2);
twoFiveNoBDec8=[0.0666 0.0845];
%twoFiveNoBDec8(1)=[];
twoFiveWBDec8=[0.0839 0.0896 0.0864];
fourtyNoBDec8=[0.0776 0.0476 0.0537];
fourtyNoBDec8(2:3)=[];
sixtyNoBDec8=[0.0771];
sixtyWBDec8=[0.1125 0.0848];
sixtyWBDec8(1)=[];
baseDec8=[0.0638 0.0731];
aveDec8=[mean(fiveNoBDec8) mean([tenNoBDec8 tenWBDec8]) mean(fifteenNoBDec8) mean([twoFiveNoBDec8 twoFiveWBDec8]) mean([fourtyNoBDec8]) mean([sixtyNoBDec8 sixtyWBDec8]) mean([baseDec8])];
aveDecAll=aveDec1+aveDec4+aveDec8;
aveDecAll=aveDecAll/3

aveAll
aveAll=aveAll;
aveDecAll=aveDecAll;
%aveDecAll=log10(aveDecAll);
%aveAll=log10(aveAll);

DBs=[5 10 15 25 40 60 80];
plot(DBs,aveAll,'-^',DBs,aveDecAll,'-*');
title('Bit Error Rate versus SNR using optical communication and Red Pitayas');
xlabel('SNR (dB)');
ylabel('BER (%)');
legend('No FEC', '1/2 rate 15 11 code with constraint length 4 ');