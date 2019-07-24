
/***********************************************************************
 * |PothosDoc Convolution Code Encoder
 *
 * This custom block implments viterbi decoding. Maximum constraint of 8 for this implementation. Also 1 bit input for now
 *
 * |category /Custom
 * |factory /Custom/CCEncoder()
 **********************************************************************/
#include <Pothos/Framework.hpp>
#include <math.h>
#include <stdlib.h> 
#include <vector> 
class ViterbiNode{
public: 	
	ViterbiNode(){}
	ViterbiNode(int nodeIndex){
		trellisIndex=nodeIndex;
	}
	void addPath(std::vector<int> toCopy, int newPathHamming){
		

		if(pathHamming==-1){
			for(uint8_t i=0;i<path.size();i++){
				prevPath.push_back(path[i]);			
			}
			prevPathHamming=pathHamming;
			for(uint8_t i=0;i<toCopy.size();i++){
				path.push_back(toCopy[i]);		
			}	
			pathHamming=newPathHamming;
		}
		else if(newPathHamming<=pathHamming&&toCopy.size()>path.size()){	
			for(uint8_t i=0;i<path.size();i++){
				prevPath.push_back(path[i]);			
			}
			prevPathHamming=pathHamming;
			for(uint8_t i=0;i<toCopy.size();i++){
				path.push_back(toCopy[i]);		
			}	
			pathHamming=newPathHamming;
		} else if(newPathHamming==pathHamming&&toCopy.size()==path.size()){
			if(rand()%2){			
				for(uint8_t i=0;i<path.size();i++){
					prevPath.push_back(path[i]);			
				}
				prevPathHamming=pathHamming;
				for(uint8_t i=0;i<toCopy.size();i++){
					path.push_back(toCopy[i]);		
				}	
				pathHamming=newPathHamming;
			}
		}
	}		
	
	int getPathHamming(){return pathHamming;}
	int getPrevPathHamming(){return prevPathHamming;}		
	int getPathLength(){return path.size();}
	int getPrevPathLength(){return prevPath.size();}
	void deletePath(){
		path.clear();
		prevPath.clear();
		pathHamming=-1;
		prevPathHamming=-1;	
	}
	~ViterbiNode(){}

private:
	int pathHamming=-1;	
	int prevPathHamming=-1;
	std::vector<int> path;	
	std::vector<int> prevPath;

	//ViterbiNode *nextNode=NULL;
	int trellisIndex=0;
	bool nodeAlloc=false;


};
class CCDecoder: public Pothos::Block
{
public:
	CCDecoder(){
		this->setupInput(0,typeid(int));
		this->setupOutput(0,typeid(int));  
		
	}
    	static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new CCDecoder();
	}
	void work(void){
		auto inputPort = this->input(0);
		auto outputPort=this->output(0);
		const uint8_t *inputBuffer=inputPort->buffer();
		uint8_t *outputBuffer=outputPort->buffer();
		bool* inBuffer=NULL;
		bool* outBuffer=NULL; 	
		bool* flushBuffer=NULL;

		const size_t numElems=inputPort->elements();
		const size_t numElemsOut=outputPort->elements();
		if(numElems<=0)
			return;
		inBuffer=new bool[numElems*8];
		size_t flushBits=constraint*rate;
		size_t flushBytes=flushBits/8;
		flushBytes+=(flushBits%8)>0?1:0;

		flushBytes+=(flushBits%8)>0?1:0;
		if((numElemsOut-numElems)<=flushBytes){
			//skip=true;
			//flushBytes=0;
			//flushBits=0;		
		}
			//flushBytes=0;
			//flushBits=0;
		outBuffer=new bool[numElems*8/rate];	
		//outBuffer=new bool[numElems*8*rate+flushBits];	
		flushBuffer=new bool[flushBits];
		BytesToBool(inputBuffer,inBuffer,numElems);
		Decode(inBuffer,outBuffer,numElems*8);
		size_t outCount=(numElems/rate);
		//outCount+=flushBytes;
		//BoolToBytes(outBuffer,outputBuffer,outCount );
		BoolToBytes(outBuffer,outputBuffer,outCount );
	
		inputPort->consume(numElems);
		//inputPort->clear();
		outputPort->produce(outCount);





		delete inBuffer;
		inBuffer=NULL;
		delete outBuffer;
		outBuffer=NULL;	
		delete flushBuffer;
		flushBuffer=NULL;
	}

private:
	int constraint =7;
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
	ViterbiNode ** nodes;
	void Decode(const bool* inBuffer,bool*outBuffer, const size_t numIn ){
		codes=new int[rate];
		codes[0]=79;
		codes[1]=109;

		buildTrellis(constraint,codes,rate);
		stateCount=(int)pow(2,constraint);
		nodes=new ViterbiNode*[stateCount];
		for(int i=0;i<stateCount;i++){
			nodes[i]=new ViterbiNode(i);		
		}
		
		delete codes;
		delete nodes;
		nodes=NULL;
		codes=NULL;
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
};

static Pothos::BlockRegistry registerMyBlock(
    "/Custom/CCEncoder", &CCDecoder::make);
