
/***********************************************************************
 * |PothosDoc Convolution Code Encoder
 *
 * This custom block implments convolutional code, 1/2 rate codes currently supported. Buffer reallocated and sent again. Add polynomials in variables
 *
 * |category /Custom
 * |param polyF[Polynomial First ] First decimal polynomial representation
 * |default 15
 * |param polyS[Polynomial Second ] Second decimal polynomial representation
 * |default 11 
 * |param constraint[Constraint K] Constraint Length
 * |default 4 
 * |param frameLen[Frame Length] Frame Length (Bytes)
 * |default 24 
 * |factory /Custom/CCEncoder()
 * |setter setPolyF(polyF)
 * |setter setPolyS(polyS)
 * |setter setConstraint(constraint)
 * |setter setFrameLength(frameLen)
 **********************************************************************/
#include <Pothos/Framework.hpp>
#include <math.h>
#include <stdlib.h> 
#include <vector> 
#include <complex>
#include <cstring> //memcpy
#include <algorithm> //min/max
class CCEncoder: public Pothos::Block
{
public:
	CCEncoder(){

		this->setupInput(0,"uint8");
		this->setupOutput(0,"uint8"); 
		this->registerCall(this, POTHOS_FCN_TUPLE(CCEncoder, setPolyF));
 		this->registerCall(this, POTHOS_FCN_TUPLE(CCEncoder, setPolyS));
 		this->registerCall(this, POTHOS_FCN_TUPLE(CCEncoder, setConstraint));
	 		this->registerCall(this, POTHOS_FCN_TUPLE(CCEncoder, setFrameLength));
		//	codes=new uint8_t[rate];
	}
    	static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new CCEncoder();
	}
	void setPolyF(int poly0){
		uint8_t toPush=(uint8_t)poly0;
		codes.push_back(toPush);
	}
	
	void setPolyS(int poly1){
		uint8_t toPush=(uint8_t)poly1;
		codes.push_back(toPush);
	}
		void setConstraint(int k){
		constraint=(uint8_t)k;
	}
		void setFrameLength(int len){
		frameLength=(size_t)len;
	}
    void activate(void)
    {
        done = false;
        flush=false;
        outElems = Pothos::BufferChunk();
    }
	void work(void){
		if(done){
			//return;
			done=false;
		}
		auto inputPort = this->input(0);
		auto outputPort=this->output(0);
		auto outputBuffer=outputPort->buffer();
		const uint8_t *inputBuffer=inputPort->buffer();
		bool* inBuffer=NULL;
		bool* outBuffer=NULL;

		size_t outCount;

		if(outElems.length==0){
			
			numElems=std::min(inputPort->elements(),frameLength-procCount);
			procCount+=numElems;
			outCount=(numElems*rate);
			//outCount+=(flushBits%8)>0?1:0;
			size_t flushBits=constraint*rate;
			size_t flushBytes=flushBits/8;
			flushBytes+=(flushBits%8)>0?1:0;
			if(procCount==frameLength){
				flush=true;
				//outCount+=flushBytes
				procCount=0;
			}

			outElems=Pothos::BufferChunk(Pothos::DType("uint8"),outCount);
			uint8_t *temp=new uint8_t [outCount];
			inBuffer=new bool[numElems*8];

			outBuffer=new bool[numElems*8*rate];	

			BytesToBool(inputBuffer,inBuffer,numElems);
			encode(inBuffer,outBuffer,numElems*8);
			BoolToBytes(outBuffer,temp,outCount );
			std::memcpy(outElems.as<void *>(),temp,outCount);

			delete temp;
			temp=NULL;
		}
		

		
		const auto outElemCount=std::min(outElems.elements(),outputPort->elements());
		std::memcpy(outputBuffer.as<void *>(),outElems.as<const void *>(),outElemCount);		
		outputPort->produce(outElemCount);
		outElems.address+=outElemCount;
		outElems.length-=outElemCount;
		if(outElems.length==0){
			inputPort->consume(numElems);
			done=true;
			delete inBuffer;
			inBuffer=NULL;
			delete outBuffer;
			outBuffer=NULL;	
			//delete tempFlushBuffer;
			//tempFlushBuffer=NULL;
		}

	}

private:
	uint8_t constraint =0;
	int rate =2;
	int bitsIn=1;
	std::vector<uint8_t> codes;
	bool** polyCodes=NULL;
	bool * codeBuffer=NULL;
	bool skip=true;
	bool flush=false;
    Pothos::BufferChunk outElems;
    bool done=false;
    size_t numElems=0;
    size_t frameLength;
    size_t procCount=0;
	void encode(bool* inBuffer,bool*outBuffer, const size_t numIn){

		//codes.push_back(15);
		//codes.push_back(11)	;	
		polyCodes=new bool*[rate];
		
		for(auto i=0;i<rate;i++){
			polyCodes[i]=new bool[constraint];
			for(auto j=0;j<constraint;j++){
				polyCodes[i][j]=0;
				polyCodes[i][j]=getBit(codes[i],j);
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
		if(flush){
			flush=false;
			for(size_t i=numIn;i<constraint+numIn;i++){
				for(int j=constraint-1;j>bitsIn-1;j--){
					codeBuffer[j]=codeBuffer[j-1]	;		
				}
				for(int j=bitsIn-1;j>-1;j--){
					codeBuffer[j]=0	;		
				}
				/*
				for(int j=0;j<rate;j++){
					bool out=0;
					for(int k=0;k<constraint;k++){
						bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k];
						out=XOR(out,poly);
					}
					*(outBuffer+i*rate+j)=out;	
				}	
				*/
			}
		}

		for(auto i=0;i<rate;i++){
			delete polyCodes[i];
			polyCodes[i]=NULL;
		}
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
