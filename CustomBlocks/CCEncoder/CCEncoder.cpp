
/***********************************************************************
 * |PothosDoc Convolution Code Encoder
 *
 * This custom block implments convolutional code
 *
 * |category /Custom
 * |factory /Custom/CCEncoder()
 **********************************************************************/
#include <Pothos/Framework.hpp>
class CCEncoder: public Pothos::Block
{
public:
	CCEncoder(){
		this->setupInput(0,typeid(int));
		this->setupOutput(0,typeid(int));  
		
	}
    	static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new CCEncoder();
	}
	void work(void){
		auto inputPort = this->input(0);
		auto outputPort=this->output(0);

		const size_t numElems=inputPort->elements();
		int* codes=new int[rate];
		codes[0]=79;
		codes[1]=109;
		encode(inputPort->buffer(),outputPort->buffer(),numElems);
		const size_t numElemsOut=outputPort->elements();
		outputPort->produce(numElemsOut);
	}

private:
	int constraint =7;
	int rate =2;
	int bitsIn=1;
	int* codes=NULL;
	bool** polyCodes=NULL;
	bool * codeBuffer=NULL;
	
	void encode(const bool* inBuffer,bool*outBuffer, const size_t numIn ){
		polyCodes=new bool*[rate];
		for(auto i=0;i<rate;i++){
			polyCodes[i]=new bool[constraint];
			for(auto j=0;j<constraint;j++){
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
				codeBuffer[j]=inBuffer[i+bitsIn-1-j]	;		
			}
			for(int j=0;j<rate;j++){
				bool out=0;
				for(int k=0;k<constraint;k++){
					bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k]
;
					out=XOR(out,poly);
				}
				outBuffer[i*rate+j]=out;			
			}	
		}
		for(size_t i=numIn;i<constraint+numIn;i++){
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
				outBuffer[i*rate+j]=out;	
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
	bool XOR(bool A, bool B){
		return A!=B	;
	}
	bool getBit(unsigned char byte, int position)
	{
	    return (byte >> position) & 0x1;
	}
};
static Pothos::BlockRegistry registerMyBlock(
    "/Custom/CCEncoder", &CCEncoder::make);
