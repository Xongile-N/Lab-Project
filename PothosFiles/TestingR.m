%% Define Red Pitaya as TCP/IP object
clc
clear all
close all
IP= '10.0.0.100';           % Input IP of your Red Pitaya...
port = 1001;
tcpipObj=tcpip(IP, port);

tcpipObj.InputBufferSize = 16384*64;
tcpipObj.OutputBufferSize = 16384*64;
flushinput(tcpipObj)
flushoutput(tcpipObj)

%% Open connection with your Red Pitaya and close previous
x=instrfind;
fclose(x);
fopen(tcpipObj);
tcpipObj.Terminator = 'CR/LF';

%% Calcualte arbitrary waveform with 16384 samples
% Values of arbitrary waveform must be in range from -1 to 1.
N=16383;
t=0:(2*pi)/N:2*pi;
x=sin(t)+1/3*sin(3*t);
y=1/2*sin(t)+1/4*sin(4*t);
plot(t,x,t,y)
grid on

%% Convert waveforms to string with 5 decimal places accuracy
waveform_ch_1_0 =num2str(x,'%1.5f,');
waveform_ch_2_0 =num2str(y,'%1.5f,');

% latest are empty spaces  “,”.
waveform_ch_1 =waveform_ch_1_0(1,1:length(waveform_ch_1_0)-3);
waveform_ch_2 =waveform_ch_2_0(1,1:length(waveform_ch_2_0)-3);

%%

fprintf(tcpipObj,'GEN:RST')                     % Reset to default settings
fprintf(tcpipObj,'ACQ:RST');
fprintf(tcpipObj,'ACQ:DEC 1');
fprintf(tcpipObj,'ACQ:TRIG:LEV 0');
fprintf(tcpipObj,'ACQ:TRIG:DLY 0');

fprintf(tcpipObj,'SOUR1:FUNC ARBITRARY');       % Set function of output signal

fprintf(tcpipObj,['SOUR1:TRAC:DATA:DATA ' waveform_ch_1])  % Send waveforms to Red Pitya

fprintf(tcpipObj,'SOUR1:VOLT 0.7');             % Set amplitude of output signal

fprintf(tcpipObj,'SOUR1:FREQ:FIX 4000');        % Set frequency of output signal


fprintf(tcpipObj,'OUTPUT1:STATE ON');
% fprintf(tcpipObj,'ACQ:START');
% fprintf(tcpipObj,'ACQ:TRIG CH1_PE');
% 
% pause(1)
% while 1
%      trig_rsp=query(tcpipObj,'ACQ:TRIG:STAT?')
% 
%      if strcmp('TD',trig_rsp(1:2))  % Read only TD
% 
%      break
% 
%      end
% end
%  signal_str=query(tcpipObj,'ACQ:SOUR1:DATA?');
% signal_str_2=query(tcpipObj,'ACQ:SOUR2:DATA?');
% 
% % Convert values to numbers.% First character in string is “{“
% % and 2 latest are empty spaces and last is “}”.
% 
% signal_num=str2num(signal_str(1,2:length(signal_str)-3));
% signal_num_2=str2num(signal_str_2(1,2:length(signal_str_2)-3));
% 
% plot(signal_num)
% hold on
% plot(signal_num_2,'r')
% grid on
% ylabel('Voltage / V')
% xlabel('samples')
fclose(tcpipObj)