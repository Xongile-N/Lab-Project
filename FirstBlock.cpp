#include <Pothos/Framework.hpp>

class SquareFloat: public Pothos::Block
{
public:
    SquareFloat(args...)
	{
	        //a constructor can initialize the block's settings, 			ports, etc...
		this->setupInput(0,typeid(float));
		this->setupOutput(0,typeid(float));    
	}

    static Block *make(args...)
	{
	        //a factory function to create an instance of MyBlock
	        return new MyBlock(args...);
	}

    void work(void)
	{
		auto inputPort = this->input(0);
		auto outputPort=this->output(0);
		const float *inputBuffer=inputPort->buffer();
		const float *outputBuffer=outputPort->buffer();
		const size_t numElems=inputPort->elements();
		for(auto i=0;i<numElems;i++){
			*outputBuffer++=square(&(inputBuffer+i))
		}	        
		inputPort->consume(numElems);
		outputPort->produce(numElems);

	}
private:
	float square(float toSquare)
	{
		return toSquare*toSquare;	
	}


};

//register MyBlock into the block registry
static Pothos::BlockRegistry registerSquareFloat(
    "~/Lab-Project/customBlocks", &SquareFloat::make);
