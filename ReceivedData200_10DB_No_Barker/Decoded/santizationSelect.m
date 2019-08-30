clc;
fprintf('Start of run. \n\n');

%file = fopen('QPSKRandSync.dat');
%file = fopen('DBPSK_20MB_No_FEC_450Bytes.dat');
%file = fopen('File3.bin');
%file = fopen('A.bin');
file = fopen('TestData_200.dat');
A = fread(file);
frewind(file);
bitsA = fread(file, '*bit1', 'ieee-be');
fclose(file);

%file = fopen('TestData.dat');
%file = fopen('TestData_450.dat');
%file = fopen('File4.bin');
%file = fopen('B.bin');
file = fopen('DBPSK_FEC_200_15_11_4_8_1_Decoded.dat');
B = fread(file);
frewind(file);
bitsB = fread(file, '*bit1', 'ieee-be');
fclose(file);

bitDiffCount = 0;
sizeA = length(bitsA);
sizeB = length(bitsB);
if sizeA < sizeB
  smallerArray = bitsA;
  largerArray = bitsB;
  len = sizeB;
elseif sizeB < sizeA
  smallerArray = bitsB;
  largerArray = bitsA;
  len = sizeA;
else
  smallerArray = bitsA;
  largerArray = bitsB;
  len = sizeA;
end
extendedArray = [repmat(smallerArray, floor(len / numel(smallerArray)), 1); smallerArray(1:mod(len, numel(smallerArray)))];

errorIndex = zeros(1000000000,1);
% errorIndex = errorIndex';
bitDiffCount = 0;
checkLength = length(smallerArray); %Check length of 80=10B
offset = 0;
offsetIncrement = length(smallerArray);% length(smallerArray);
len = len - mod(len, checkLength)
rounds = ceil(len/checkLength)
%rounds=2000

roundDiff = zeros(rounds,1);
roundBER = zeros(rounds,1);
tic
for i=1:rounds
  for j=1:length(smallerArray)
    if smallerArray(j)~=largerArray(j+offset)
      bitDiffCount = bitDiffCount + 1;
      errorIndex(j+offset) = 1;
    end
  end
  roundDiff(i) = bitDiffCount;
  roundBER(i) = (bitDiffCount/checkLength)*100;
  bitDiffCount = 0;
  offset = offset + offsetIncrement;
%   largerArray = circshift(largerArray,length(smallerArray)-1);
end

%roundDiff
roundBER.'
weightedAve=[];
offset=1
index=1;
while index<length(roundBER)
    if(roundBER(index)<40)
        weightedAve(offset)=roundBER(index);
        offset=offset+1;
        
    end
    index=index+1;
end
avg = mean(roundBER)
ave=mean(weightedAve)
offset
% len = 5e5%8e7%5e5
% difference = zeros(len,1);
% for i=1:len %32
%   difference(i) = abs(largerArray(i) - extendedArray(i));
% end
if sizeA==sizeB
  fprintf('These files are the same size. They have length %db(%dB). \n', sizeA, sizeA/8);
else
  fprintf('These files are not the same size. File A has length %db(%dB) while file B has length %db(%dB). \n', sizeA, sizeA/8, sizeB, sizeB/8);
end

% errorPos = find(difference);
% errorPos(1:30)
% 
% length(errorPos)
% BER = (length(errorPos)/len)*100
% 
% plot((1:length(difference)),difference)
%plot((1:length(roundBER)),roundBER)
% ax = gca;
% ax.XRuler.Exponent = 0;
% ylim([-0.5 1.5])
%disp(difference.')