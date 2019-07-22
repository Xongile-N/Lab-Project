
/***********************************************************************
 * |PothosDoc SquareFloat
 *
 * This custom block squares incoming floats and gives that as ouptut
 *
 * |category /Custom
 * |factory /Custom/SquareFloat()
 **********************************************************************/
#include <Pothos/Framework.hpp>

class SquareFloat: public Pothos::Block
{
public:
    SquareFloat()
	{
		this->setupInput(0,typeid(float));
		this->setupOutput(0,typeid(float));    
	}

    static Block *make()
	{
	        //a factory function to create an instance of MyBlock
	        return new SquareFloat();
	}

    void work(void)
	{

		auto inputPort = this->input(0);
		auto outputPort=this->output(0);
		const float *inputBuffer=inputPort->buffer();
		float *outputBuffer=outputPort->buffer();
		const size_t numElems=inputPort->elements();
				
		for(size_t i=0;i<numElems;i++)
		{
			//auto inc=i*(inputPort->dtype().size() );
			auto inc=i;
			//*outputBuffer++=0.0f;
			*outputBuffer++=square(*(inputBuffer+inc) );
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
static Pothos::BlockRegistry registerMyBlock(
    "/Custom/SquareFloat", &SquareFloat::make);
