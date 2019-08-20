clear all;
%Decided on 11 8
clc;
b13=[1 1 1 1 1 0 0 1 1 0 1 0 1];
b13conv=b13*2-1;
b39conv=[b13conv b13conv b13conv];
code=[0 1 1 1 1 1 0 0 1 1 0 1 0 1 0 0];
b1=[0 0 1 1 1 0 1 1];
b2=[1 1 1 1 1 0 1 1];
b3=[0 0 1 0 0 0 1 0];
b4=[0 0 0 0 1 1 1 0];
b5=[0 0 1 1 0 1 1 0];
b6=[0 1 1 0 0 0 0 0];
codeFirst8=[code   b1 b2 b3 b4 b5 b6];
%codeConv=codeFirst8*2-1;
codeConv=b13conv;
corrThresh=11;

frameLength=402;
frameLength=8*frameLength;
file="DBPSK_FEC_200_15_11_4_5_0_Barker.dat";
outFile="DBPSK_FEC_200_15_11_4_5_0_Barker_Trimmed.dat";
fileID=fopen(file);
outFileID=fopen(outFile,'w');

data=fread(fileID);
%de2bi(254,'left-msb');
dataBin=de2bi(data,'left-msb');
dataBin=dataBin';
dataBinColumn=reshape(dataBin,1,[]);
%length(datadataBinColumn);
index=1;
len=length(dataBinColumn);
len=min(len,160000000);
corrs=zeros(1,len);
codeConva=codeConv;
codeConva(1)=1;
dataCleaned=ones(1,len);
dataCleaned=dataCleaned*10;
xcorr(codeConv,codeConv,0)
count=0;
codeLen=length(codeConv)
header=zeros(codeLen);
indexOffset=1;
while index <len
   if(index+frameLength>len)
        break;
   end
   header=dataBinColumn(index+indexOffset:index+indexOffset+codeLen-1);

   header=header*2-1;
   corr=xcorr(header,codeConv,0);
   if(corr>corrThresh)
       index
       %header=header/2+0.5
       %dataBinColumn(index+16:index+16+31)

      dataCleaned(index+16:index+frameLength-1)=dataBinColumn(index+16:index+frameLength-1);
      index=index+frameLength;
      count=count+frameLength-16;
    %index-1
   else 
       index=index+8;
   end
end
count;
offset=1;

dataPrePack=ones(1,count);
for index=1:len
    if(dataCleaned(index)~=10)
        dataPrePack(offset)=dataCleaned(index);
        offset=offset+1;
    end
end
dataPrePack=reshape(dataPrePack,8,[])';
finalData=bi2de(dataPrePack,'left-msb');
fwrite(outFileID,finalData);
fclose(outFileID);
fclose(fileID);
%plot(xcorr(codeConv,codeConv));
%plot(corrs(1:len));