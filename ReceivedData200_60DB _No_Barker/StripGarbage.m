clear all;
%Decided on 11 8
clc;


frameLength=400;
frameLength=8*frameLength;
origFile="TestData_200_Encoded_15_11_4_8.dat";

file="DBPSK_FEC_200_15_11_4_8_2.dat";
outFile="DBPSK_FEC_200_15_11_4_8_2_Trimmed_Scuffed.dat";
origFileID=fopen(origFile);
fileID=fopen(file);
outFileID=fopen(outFile,'w');

data=fread(fileID);
dataBin=de2bi(data,'left-msb');
dataBin=dataBin';
dataBinColumn=reshape(dataBin,1,[]);
origData=fread(origFileID);
origDataBin=de2bi(origData,'left-msb');
origDataBin=origDataBin';
origDataBinColumn=reshape(origDataBin,1,[]);
headerLength=4*8;
footerLength=4*8;
headerErrThresh=5;
footerErrThresh=5;
headerOrig=origDataBinColumn(1:headerLength);
footerOrig=origDataBinColumn(end-footerLength+1:end);
headerOrig=headerOrig*2-1;
footerOrig=footerOrig*2-1;

increment=8;
index=1;
len=length(dataBinColumn);
len=min(len,160000000);

dataCleaned=ones(1,len);
dataCleaned=dataCleaned*10;
count=0;
header=zeros(headerLength);
footer=zeros(footerLength);
indexOffset=1;
while index <len
    index
     if(index+frameLength>len)
          break;
     end
     header=dataBinColumn(index:index+headerLength-1);
     footer=dataBinColumn(index+frameLength-footerLength:index+frameLength-1);
  
     header=header*2-1;
     footer=footer*2-1;
     errVecH=abs(header-headerOrig)/2;
     errVecF=abs(footer-footerOrig)/2;
     errH=sum(errVecH);
     errF=sum(errVecF);
     if(errH<=headerErrThresh&&errF<=footerErrThresh)
            index*-1
            dataCleaned(index:index+frameLength-1)=dataBinColumn(index:index+frameLength-1);
            count=count+frameLength;
            index=index+frameLength;
     else 
        index=index+increment;
    end
 end

 offset=1;
 
 dataPrePack=ones(1,count);
 for index=1:len
     if(dataCleaned(index)~=10)
         dataPrePack(offset)=dataCleaned(index);
         offset=offset+1;
     end
 end
 offset
 dataPrePack=reshape(dataPrePack,8,[])';
 finalData=bi2de(dataPrePack,'left-msb');
 fwrite(outFileID,finalData);
fclose(outFileID);
fclose(origFileID);
fclose(fileID);
%plot(xcorr(codeConv,codeConv));
%plot(corrs(1:len));