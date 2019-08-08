
/***********************************************************************
 * |PothosDoc SymbolsToSamples
 *
 * This custom block outputs N samples for every symbol in. Rates listed are all suitable for 1.25e6 Hz signal
 * Should split and recombine the data
 * |category /Custom
 * |param samps The number of smaples per symbol
 * |option 1
 * |option 2
 * |option 4
 * |option 5
 * |option 8
 * |option 10
 * |option 16
 * |option 20
 * |option 25
 * |option 40
 * |option 50
 * |option 80
 * |option 100
 * |option 125
 * |option 200
 * |option 250
 * |option 400
 * |option 500
 * |option 625
 * |option 1000
 * |option 1250
 * |option 2000
 * |option 2500
 * |option 3125
 * |option 5000
 * |option 6250
 * |option 12500
 * |option 15625
 * |option 25000
 * |option 32150
 * |option 50000
 * |option 62500
 * |option 78125
 * |option 125000
 * |option 156250
 * |option 250000
 * |option 312500
 * |option 625000
 * |option 1250000
 * |param dtype[Data Type] The data type.
 * |widget DTypeChooser(float=1,int=1,dim=1)
 * |default "complex_float64"
 * |preview disable
 * |factory /Custom/SymbolsToSamples(dtype)
 * |setter setSamps(samps)
 **********************************************************************/
#include <Pothos/Framework.hpp>
#include <math.h>
#include <stdlib.h> 
#include <vector> 
#include <complex>
#include <cstring> //memcpy
#include <algorithm> //min/max
#include <iostream>

class SymbolsToSamples: public Pothos::Block
{
public:
	SymbolsToSamples(const Pothos::DType &dtype){

		this->setupInput(0,dtype);
		this->setupOutput(0,dtype); 
		this->registerCall(this, POTHOS_FCN_TUPLE(SymbolsToSamples, setSamps));
 		//	codes=new uint8_t[rate];
	}
    	static Block *make(const Pothos::DType &dtype)
	{
	        //a factory function to create an instance of MyBlock
	        return new SymbolsToSamples(dtype);
	}
	void setSamps(int new_samps){
			samps=new_samps;
	}
    void activate(void)
    {
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

		numElems=inputPort->elements();
		if(numElems==0)return;
		if(outElems.length==0){
			elemSize=outputPort->dtype().size();
			//elemSize=2;
			size_t outCount=0;
			outCount=numElems*samps*elemSize;
			outElems=Pothos::BufferChunk(Pothos::DType("uint8"),outCount	);
			//outElems=Pothos::BufferChunk(inputPort->dtype(),samps	);
			for(size_t i=0;i<numElems;i++){
				//auto val=inputBuffer.as<const void *>()+(i*elemSize);
				const void* val=inputBuffer+(i*elemSize);
				for(int j=0;j<samps;j++){
					size_t offset=(j+i*samps)*elemSize;
					std::memcpy(outElems.as<void *>()+offset,val,elemSize);
				}
			}

		}

		//const auto outElemCount=std::min(outElems.elements(),outputPort->elements());
		//std::memcpy(outputBuffer.as<void *>(),outElems.as<const void *>(),outElemCount);		
		//outputPort->produce(outElemCount/elemSize);
		//std::cout<<"outElem"<<outElemCount<<std::endl;
		outputPort->postBuffer(outElems);
		std::cout<<outElems.length<<std::endl;
		//outElems.address+=outElemCount;
		//outElems.length-=outElemCount;
				outElems.length=0;
		if(outElems.length==0){
			inputPort->consume(numElems);
		}

	}

private:
//int sampRate=1250000;
//int baudIndex=0;
//std::vector<int>bauds;
int samps=1;
bool done=false;
    Pothos::BufferChunk outElems;
    int produced=0;
    size_t numElems=0;
    size_t elemSize=0;
};
static Pothos::BlockRegistry registerMyBlock(
    "/Custom/SymbolsToSamples", &SymbolsToSamples::make);
