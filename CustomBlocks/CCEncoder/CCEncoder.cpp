
/***********************************************************************
 * |PothosDoc Convolution Code Encoder
 *
 * This custom block implments convolutional code, bool array version. Byet bool conversions present.All with pointers initialised. 	 
 * Removed using any as array. V2
 *
 * |category /Custom
 * |factory /Custom/CCEncoder()
 **********************************************************************/
#include <Pothos/Framework.hpp>
class CCEncoder: public Pothos::Block
{
public:
	CCEncoder(){
		this->setupInput(0,"uint8");
		this->setupOutput(0,"uint8");  
		
	}
    	static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new CCEncoder();
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
		if((numElemsOut-numElems)<=flushBytes){
			//skip=true;
			//flushBytes=0;
			//flushBits=0;		
		}
			//flushBytes=0;
			//flushBits=0;
		outBuffer=new bool[numElems*8*rate];	
		//outBuffer=new bool[numElems*8*rate+flushBits];	
		flushBuffer=new bool[flushBits];
		BytesToBool(inputBuffer,inBuffer,numElems);
		encode(inBuffer,outBuffer,numElems*8,flushBuffer);
		size_t outCount=(numElems*rate);
		//outCount+=flushBytes;
		//BoolToBytes(outBuffer,outputBuffer,outCount );
		BoolToBytes(outBuffer,outputBuffer,outCount );
	
		inputPort->consume(numElems);
		//inputPort->clear();
		outputPort->produce(outCount);
		uint8_t *tempFlushBuffer=new uint8_t[flushBytes];
		/*
		outputPort->popElements(outCount);
		

		BoolToBytes(flushBuffer,outhPutBuffer,flushBytes );

		outputPort->produce(flushBytes);
		*/

		delete inBuffer;
		inBuffer=NULL;
		delete outBuffer;
		outBuffer=NULL;	
		delete flushBuffer;
		flushBuffer=NULL;
		delete tempFlushBuffer;
		tempFlushBuffer=NULL;

	}

private:
	uint8_t constraint =4;
	int rate =2;
	int bitsIn=1;
	uint8_t* codes=NULL;
	bool** polyCodes=NULL;
	bool * codeBuffer=NULL;
	bool skip=true;
	void encode(bool* inBuffer,bool*outBuffer, const size_t numIn,bool* bufferForFlush ){
		codes=new uint8_t[rate];
		codes[0]=13;
		codes[1]=11	;	
		polyCodes=new bool*[rate];
		
		for(auto i=0;i<rate;i++){
			polyCodes[i]=new bool[constraint];
			for(auto j=0;j<constraint;j++){
				polyCodes[i][j]=0;
				polyCodes[i][j]=getBit(*(codes+i),j);
			}
		}
		
		
		codeBuffer=new bool[constraint];
		for(auto i=0;i<constraint;i++){
			codeBuffer[i]=0;		
		}
		for(size_t i=0;i<numIn;i+=bitsIn){
			for(int j=constraint-1;j>bitsIn-1;j--){
				codeBuffer[j]=codeBuffer[j-1]	;		
			}
			for(int j=bitsIn-1;j>-1;j--){
				codeBuffer[j]=*(inBuffer+i+bitsIn-1-j)	;		
			}
			for(int j=0;j<rate;j++){
				bool out=0;
				for(int k=0;k<constraint;k++){
					bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k]
;
					out=XOR(out,poly);
				}
				*(outBuffer+i*rate+j)=out;			
			}	
		}
		if(!skip){
			for(size_t i=0;i<constraint;i++){
				for(int j=constraint-1;j>bitsIn-1;j--){
					codeBuffer[j]=codeBuffer[j-1]	;		
				}
				for(int j=bitsIn-1;j>-1;j--){
					codeBuffer[j]=0	;		
				}

				for(int j=0;j<rate;j++){
					bool out=0;
					for(int k=0;k<constraint;k++){
						bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k]
		;
						out=XOR(out,poly);
					}
					*(bufferForFlush+i*rate+j)=out;	
				}	
			}
		}

		for(auto i=0;i<rate;i++){
			delete polyCodes[i];
			polyCodes[i]=NULL;
		}
		delete codes;
		codes=NULL;
		delete polyCodes;
		polyCodes=NULL;
		delete codeBuffer;
		codeBuffer=NULL;
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
	bool XOR(bool A, bool B){
		return A!=B	;
	}
	bool getBit(unsigned char byte, int position)
	{
		//return false;
	    return (byte >> position) & 0x1;
	}
};
static Pothos::BlockRegistry registerMyBlock(
    "/Custom/CCEncoder", &CCEncoder::make);
