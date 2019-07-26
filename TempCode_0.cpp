/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
#include <math.h>
#include <stdlib.h> 
#include <vector> 
#include <time.h>
int constraint =4;
int rate =2;
uint8_t stateCount=0;
int bitsIn=1;
int* codes=NULL;
bool** polyCodes=NULL;
bool * codeBuffer=NULL;
uint8_t ** trellis;
int stateAttri=7;
int currState=0;
int zeroNext=1;
int zeroOutput=2;
int oneNext=3;
int oneOutput=4;
int prev_0=5;
int prev_1=6;
bool getBit(unsigned char byte, int position)
{
    return (byte >> position) & 0x1;
}
bool XOR(bool A, bool B){
	return A!=B	;
}
void BytesToBool(const uint8_t* oldBuff,bool* newBuff,size_t length){
	size_t offset=0;
	for(size_t i=0;i<length;i++){
		for(auto j=7;j>-1;j--){
			*(newBuff+offset)=getBit(*(oldBuff+i),j);	
			offset++;
		}	

	}
}
void BoolToBytes(bool* oldBuff,uint8_t* newBuff,size_t length){
	size_t offset=0;
	for(size_t i=0;i<length;i++){
		for(int j=0;j<8;j++){
	        *(newBuff+i)*=2;
			*(newBuff+i)+=*(oldBuff+offset);
			offset++;		

		}
	}
}
void buildTrellis(int k_constraint,int * polies,int codeRate){
	stateCount=(int)pow(2,k_constraint);
	trellis =new  uint8_t*[(stateCount)];
	polyCodes=new bool*[rate];
	for(uint8_t i=0;i<stateCount;i++){
		trellis[i]=new uint8_t[stateAttri];
		trellis[i][currState]=i;
		trellis[i][zeroNext]=i>>1;
		trellis[i][oneNext]=(i+stateCount)>>1;

	}		
	for(uint8_t i=0;i<stateCount;i++){
	    int count=0;
	    for(int j=0;j<stateCount;j++){
	        if(count==0){
	            if(trellis[i][currState]==trellis[j][zeroNext]||trellis[i][currState]==trellis[j][oneNext])
	            {
	                trellis[i][prev_0]=trellis[j][currState];
	                count++;
	            }
	        }
	        else if(count ==1){
	            if(trellis[i][currState]==trellis[j][zeroNext]||trellis[i][currState]==trellis[j][oneNext])
	            {
	                trellis[i][prev_1]=trellis[j][currState];
	                count++;
	            }
	        }
	        
	        if(count>=2)
	        break;
	    }
	}
	for(auto i=0;i<rate;i++){
		polyCodes[i]=new bool[k_constraint];
		for(auto j=0;j<k_constraint;j++){
			polyCodes[i][j]=getBit(polies[i],j);
		}
	}
	codeBuffer=new bool[k_constraint];
	for(int i=0;i<stateCount;i++){
		uint8_t outState0=0;
		uint8_t outState1=0;
		uint8_t state=trellis[i][currState];
		state=(state>>1);

		for(int i=0;i<k_constraint;i++){
		    codeBuffer[i]=getBit(state,k_constraint-1-i);
		 }
		for(int j=0;j<rate;j++){
			outState0*=2;
			outState1*=2;
			bool out0=0;
			codeBuffer[0]=0;
			for(int k=0;k<constraint;k++){
				bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k];
				out0=XOR(out0,poly);
			}
			outState0+=out0;
			codeBuffer[0]=1;

			bool out1=0;
			for(int k=0;k<constraint;k++){
				bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k];
				out1=XOR(out1,poly);
			}
			outState1+=out1;
		}
		trellis[i][zeroOutput]=		outState0;
		trellis[i][oneOutput]=		outState1;
	}

	delete polyCodes;
	polyCodes=NULL;
}
int getHammingDist(uint8_t byte_0,uint8_t byte_1){
	int hamming=0;
	for( int i=0;i<8;i++){
	    hamming+=XOR(getBit(byte_0,i),getBit(byte_1,i));
	}
	return hamming;
}

class ViterbiNode{
public: 	
	ViterbiNode(){}
	ViterbiNode(int nodeIndex){
		trellisIndex=nodeIndex;
		path.push_back(trellisIndex);
		if(trellisIndex==0){
		    pathHamming=0;
		    prevPathHamming=0;
		}else{
		    pathHamming=1000000;
		    prevPathHamming=1000000;   
		}
	}
	void addPath(const std::vector<int> toCopy, int newPathHamming){
	     if(toCopy.size()>=path.size()){
		    prevPrevPath.clear();
		    for(uint8_t i=0;i<prevPath.size();i++){
				prevPrevPath.push_back(prevPath[i]);			
			}
		    prevPath.clear();
			for(uint8_t i=0;i<path.size();i++){
				prevPath.push_back(path[i]);			
			}
			path.clear();
			prevPathHamming=pathHamming;
			for(uint8_t i=0;i<toCopy.size();i++){
				path.push_back(toCopy[i]);	
			}	
			
			path.push_back(trellisIndex);
			pathHamming=newPathHamming;
		}
		else if(toCopy.size()==prevPath.size()&&newPathHamming<pathHamming){

		    prevPrevPath.clear();
		    for(uint8_t i=0;i<prevPath.size();i++){
				prevPrevPath.push_back(prevPath[i]);			
			}
		    prevPath.clear();
			for(uint8_t i=0;i<path.size();i++){
				prevPath.push_back(path[i]);			
			}
			path.clear();
			prevPrevPathHamming=prevPathHamming;
			prevPathHamming=pathHamming;
			for(uint8_t i=0;i<toCopy.size();i++){
				path.push_back(toCopy[i]);	
			}	
			
			path.push_back(trellisIndex);
			pathHamming=newPathHamming;
		}else if(toCopy.size()<path.size()&&newPathHamming<pathHamming){
            prevPrevPath.clear();
		    for(uint8_t i=0;i<prevPath.size();i++){
				prevPrevPath.push_back(prevPath[i]);			
			}
            prevPath.clear();
			for(uint8_t i=0;i<path.size();i++){
				prevPath.push_back(path[i]);			
			}
			path.clear();
			prevPathHamming=pathHamming;
			for(uint8_t i=0;i<toCopy.size();i++){
				path.push_back(toCopy[i]);	
			}	
			
			path.push_back(trellisIndex);
			pathHamming=newPathHamming;
		}

	}		
	
	int getPathHamming(){return pathHamming;}
	int getPrevPathHamming(){return prevPathHamming;}
	int getPrevPrevPathHamming(){return prevPrevPathHamming;}		

	int getPathLength(){return path.size();}
	int getPrevPathLength(){return prevPath.size();}
	int getPrevPrevPathLength(){return prevPrevPath.size();}
    std::vector<int> getPath(){return path;}
    std::vector<int> getPrevPath(){return prevPath;}
    std::vector<int> getPrevPrevPath(){return prevPrevPath;}
	void deletePath(){
		path.clear();
		prevPath.clear();
	    prevPrevPath.clear();

		pathHamming=-1;
		prevPathHamming=-1;	
	    prevPrevPathHamming=-1;
	}
	~ViterbiNode(){}

private:
	int pathHamming=1000000;	
	int prevPathHamming=1000000;
	int prevPrevPathHamming=1000000;

	std::vector<int> path;	
	std::vector<int> prevPath;
	std::vector<int> prevPrevPath;
	int trellisIndex=0;
	bool nodeAlloc=false;


};
	ViterbiNode ** nodes;

int Decode(const bool* inBuffer,bool*outBuffer, const size_t numIn ){
	codes=new int[rate];
	codes[0]=15;
	codes[1]=11;
	int tester=0;
	buildTrellis(constraint,codes,rate);
	stateCount=(int)pow(2,constraint);
	nodes=new ViterbiNode*[stateCount];	
	for(int i=0;i<stateCount;i++){
		nodes[i]=new ViterbiNode(i);
	}
	int finalNode=0;
	int loop=12;
	int check=7;
	for(uint8_t i=0;i<numIn;i+=2){
		bool curr0=*(inBuffer+i);
		bool curr1=*(inBuffer+i+1);
		uint8_t out=curr0*2+curr1;
		if(i==0){
		    nodes[trellis[0][oneNext]]->addPath(nodes[0]->getPath(),nodes[0]->getPathHamming()+ getHammingDist(out,trellis[0][oneOutput]));	
			nodes[trellis[0][zeroNext]]->addPath(nodes[0]->getPath(),nodes[0]->getPathHamming()+ getHammingDist(out,trellis[0][zeroOutput]));
        }
		else 
		{

			for(int j=0;j<stateCount;j++){
					if(nodes[j]->getPathLength()<(i/2+1)){
					    nodes[j]->deletePath();	
                    
				    	continue;
					}
					if(nodes[j]->getPathLength()==(i/2+1)){
                        nodes[trellis[j][zeroNext]]->addPath(nodes[j]->getPath(),nodes[j]->getPathHamming()+ getHammingDist(out,trellis[j][zeroOutput]));
						if(trellis[j][zeroNext]==trellis[j][currState]){
						    nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));
						}	else{		
						    nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPath(),nodes[j]->getPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));
                        }		    
					}
					else if(nodes[j]->getPrevPathLength()==(i/2+1)){
						nodes[trellis[j][zeroNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][zeroOutput]));
					    if(trellis[j][zeroNext]==trellis[j][currState]){
						    nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPrevPath(),nodes[j]->getPrevPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));	
						}	
						else{						    
						    nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));	
                        }
					}else if(nodes[j]->getPrevPrevPathLength()==(i/2+1)){
					    nodes[trellis[j][zeroNext]]->addPath(nodes[j]->getPrevPrevPath(),nodes[j]->getPrevPrevPathHamming()+ getHammingDist(out,trellis[j][zeroOutput]));
					    nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPrevPath(),nodes[j]->getPrevPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));	
					}
			}

		}		

	}
	
	int finalHamming=10000;
    int pathLength=numIn/rate+1;
	for(int i=0;i<stateCount;i++){
		 if(nodes[i]->getPathHamming()<0||nodes[i]->getPathLength()!=pathLength){
				continue;
			}else if(nodes[i]->getPathHamming()<=finalHamming){
			    if(nodes[i]->getPathHamming()==finalHamming&&(rand()%2)==1){
			        continue;
			    }
				finalHamming=nodes[i]->getPathHamming();
				finalNode=i;
			}
	}
	std::vector<int> finalPath=nodes[finalNode]->getPath();
	for (int i=0;i<numIn/2;i++){
		*(outBuffer+i)=getBit(trellis[finalPath[i+1]][currState],constraint-1);	
	    cout<<getBit(trellis[finalPath[i+1]][currState],constraint-1);
	    
	}



	delete codes;
	delete nodes;
	nodes=NULL;
	codes=NULL;
	return finalHamming;
}


int main()
{       
        srand(time(NULL));
        bool* inBuffer=NULL;
		bool* outBuffer=NULL; 	
		bool* flushBuffer=NULL;		
		uint8_t *inputBuffer=NULL;
		inputBuffer= new uint8_t[3];
		inputBuffer[0]=226;
		inputBuffer[1]=155;
		//inputBuffer[2]=188;
		uint8_t *outputBuffer=NULL;
		outputBuffer= new uint8_t[1];
		outputBuffer[0]=1000;
		const size_t numElems=2;

		inBuffer=new bool[numElems*8];
		size_t flushBits=constraint*rate;
		size_t flushBytes=flushBits/8;
		flushBytes+=(flushBits%8)>0?1:0;

		flushBytes+=(flushBits%8)>0?1:0;
		outBuffer=new bool[numElems*8/rate];	
		flushBuffer=new bool[flushBits];
		BytesToBool(inputBuffer,inBuffer,numElems);
		int test=Decode(inBuffer,outBuffer,numElems*8);
		size_t outCount=(numElems/rate);
		BoolToBytes(outBuffer,outputBuffer,outCount );
	    cout<<endl<<test<<endl<<+outputBuffer[0];
		delete inBuffer;
		inBuffer=NULL;
		delete inputBuffer;
		inputBuffer=NULL;
		delete outputBuffer;
		outputBuffer=NULL;
		delete outBuffer;
		outBuffer=NULL;	
		delete flushBuffer;
		flushBuffer=NULL;

    return 0;
}
