
/***********************************************************************
 * |PothosDoc SymbolsToSamples
 *
 * This custom block outputs N samples for every symbol in. Rates listed are all suitable for 1.25e6 Hz signal
 *
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
 * |factory /Custom/SymbolsToSamples()
 * |setter setSamps(samps)
 **********************************************************************/
#include <Pothos/Framework.hpp>
#include <math.h>
#include <stdlib.h> 
#include <vector> 
#include <complex>
#include <cstring> //memcpy
#include <algorithm> //min/max
class SymbolsToSamples: public Pothos::Block
{
public:
	SymbolsToSamples(){

		this->setupInput(0,"uint8");
		this->setupOutput(0,"uint8"); 
		this->registerCall(this, POTHOS_FCN_TUPLE(SymbolsToSamples, setSamps));
 		//	codes=new uint8_t[rate];
	}
    	static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new SymbolsToSamples();
	}
	void setSamps(int new_samps){
			samps=new_samps;
	}
    void activate(void)
    {
        done = false;
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


		if(outElems.length==0){
			numElems=inputPort->elements();
			outElems=Pothos::BufferChunk(Pothos::DType("uint8"),samps*numElems	);
			for(size_t i=0;i<numElems;i++){
				std::memset(outElems.as<void *>()+numElems*i*inputPort->dtype().elemSize(),*(inputBuffer+i),samps);
			}
		}
		const auto outElemCount=std::min(outElems.elements(),outputPort->elements());
		std::memcpy(outputBuffer.as<void *>(),outElems.as<const void *>(),outElemCount);		
		outputPort->produce(outElemCount);
		outElems.address+=outElemCount;
		outElems.length-=outElemCount;
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
    size_t numElems;
};
static Pothos::BlockRegistry registerMyBlock(
    "/Custom/SymbolsToSamples", &SymbolsToSamples::make);
