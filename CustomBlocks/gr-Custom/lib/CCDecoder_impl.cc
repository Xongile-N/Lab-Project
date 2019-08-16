/* -*- c++ -*- */
/* 
 * Copyright 2019 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "CCDecoder_impl.h"
	ViterbiNode::ViterbiNode(){}
	ViterbiNode::ViterbiNode(int nodeIndex){
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
	void ViterbiNode::addPath(const std::vector<int> toCopy, int newPathHamming){
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
	
	int ViterbiNode::getPathHamming(){return pathHamming;}
	int ViterbiNode::getPrevPathHamming(){return prevPathHamming;}
	int ViterbiNode::getPrevPrevPathHamming(){return prevPrevPathHamming;}		

	int ViterbiNode::getPathLength(){return path.size();}
	int ViterbiNode::getPrevPathLength(){return prevPath.size();}
	int ViterbiNode::getPrevPrevPathLength(){return prevPrevPath.size();}
  std::vector<int> ViterbiNode::getPath(){return path;}
  std::vector<int> ViterbiNode::getPrevPath(){return prevPath;}
  std::vector<int> ViterbiNode::getPrevPrevPath(){return prevPrevPath;}
	void ViterbiNode::deletePath(){
		path.clear();
		prevPath.clear();
	    prevPrevPath.clear();

		pathHamming=-1;
		prevPathHamming=-1;	
	    prevPrevPathHamming=-1;
	}
	ViterbiNode::~ViterbiNode(){}
namespace gr {
  namespace Custom {

    CCDecoder::sptr
    CCDecoder::make(int constraint, int frameLength, std::vector<int> polys)
    {
      return gnuradio::get_initial_sptr
        (new CCDecoder_impl(constraint, frameLength, polys));
    }

    /*
     * The private constructor
     */
    CCDecoder_impl::CCDecoder_impl(int constraint, int frameLength, std::vector<int> polys)
      : gr::sync_decimator("CCDecoder",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)), rate),
              _constraint(constraint),
              _frameLength(frameLength)   

    {
      std::cout<<_frameLength<<"Made"<<rate<<std::endl;
      for(int i=0;i<rate;i++){
        codes.push_back((uint8_t)polys[i]);
      }
              done = false;
        flush=false;
      buildTrellis(_constraint,codes,rate);
    }

    /*
     * Our virtual destructor.
     */
    CCDecoder_impl::~CCDecoder_impl()
    {
    }

    int
    CCDecoder_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      std::cout<<"running"<<std::endl;
      int offset=0;
      const  uint8_t*in = (const uint8_t *) input_items[0];
      uint8_t *out = (uint8_t*) output_items[0];
      int produced=0;
      produced=noutput_items;
      for(int j=0;j<noutput_items;j++){
        out[j]=in[j];
      }
      /*
      size_t outCount=0;
      numElems=_frameLength*rate;
      procCount=numElems;
      size_t flushBits=_constraint*rate;
      size_t flushBytes=flushBits/8;
      flushBytes+=(flushBits%8)>0?1:0;

      for(int i=0;i<noutput_items;i++){
        procCount+=rate;
        std::cout<<procCount<<std::endl;
        if(procCount==_frameLength*rate){
          procCount=0;
          bool* inBuffer=NULL;
          bool* outBuffer=NULL; 	          
          inBuffer=new bool[numElems*8];
          outBuffer=new bool[numElems*8/rate];
          BytesToBool(in+offset*rate,inBuffer,numElems);
          decodeOutput=Decode(inBuffer,outBuffer,numElems*8);
          outCount=(numElems/rate);
          uint8_t *temp=new uint8_t [outCount];
          BoolToBytes(outBuffer,temp,outCount );
          for(int j=0;j<noutput_items;j++){
            out[j+offset]=temp[j];
            produced++;
          }
          offset+=_frameLength;
          delete temp;
          temp=NULL;
          delete inBuffer;
          inBuffer=NULL;
          delete outBuffer;
          outBuffer=NULL;	
        }
      }
      // Do <+signal processing+>
      consume_each(produced*rate); 

      */
      //consume_each(produced*rate); 
      // Tell runtime system how many output items we produced.
      return produced;
    }
    int CCDecoder_impl::Decode(const bool* inBuffer,bool*outBuffer, const size_t numIn ){
      stateCount=(int)pow(2,_constraint);
      nodes=new ViterbiNode*[stateCount];	
      for(int i=0;i<stateCount;i++){
        nodes[i]=new ViterbiNode(i);
      }
      int finalNode=0;
      for(uint8_t i=0;i<numIn;i+=rate){
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
              if(nodes[j]->getPathLength()<(i/rate+1)){
                nodes[j]->deletePath();	
                      
                continue;
              }
              if(nodes[j]->getPathLength()==(i/rate+1)){
                          nodes[trellis[j][zeroNext]]->addPath(nodes[j]->getPath(),nodes[j]->getPathHamming()+ getHammingDist(out,trellis[j][zeroOutput]));
                if(trellis[j][zeroNext]==trellis[j][currState]){
                  nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));
                }	else{		
                  nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPath(),nodes[j]->getPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));
                          }		    
              }
              else if(nodes[j]->getPrevPathLength()==(i/rate+1)){
                nodes[trellis[j][zeroNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][zeroOutput]));
                if(trellis[j][zeroNext]==trellis[j][currState]){
                  nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPrevPath(),nodes[j]->getPrevPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));	
                }	
                else{						    
                  nodes[trellis[j][oneNext]]->addPath(nodes[j]->getPrevPath(),nodes[j]->getPrevPathHamming()+ getHammingDist(out,trellis[j][oneOutput]));	
                          }
              }else if(nodes[j]->getPrevPrevPathLength()==(i/rate+1)){
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
      for (uint8_t i=0;i<numIn/rate;i++){
        *(outBuffer+i)=getBit(trellis[finalPath[i+1]][currState],_constraint-1);	
        
      }
      for(int i=0;i<stateCount;i++){
        delete nodes[i];
        nodes[i]=NULL;
      }




      delete nodes;
      nodes=NULL;


      return finalHamming;
	  }
    void CCDecoder_impl::destroyTrellis(){
      for(uint8_t i=0;i<stateCount;i++){
        delete trellis[i];

      }	
      delete trellis;
	  }
    void CCDecoder_impl::buildTrellis(int k_constraint,std::vector<uint8_t> polies,int codeRate){
      std::cout<<"Trellis Building"<<std::endl;
      stateCount=(int)pow(2,k_constraint);
      trellis =new  uint8_t*[(stateCount)];
      polyCodes=new bool*[codeRate];
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
          for(int k=0;k<_constraint;k++){
            bool poly=polyCodes[j][_constraint-k-1]&&codeBuffer[k];
            out0=XOR(out0,poly);
          }
          outState0+=out0;
          codeBuffer[0]=1;

          bool out1=0;
          for(int k=0;k<_constraint;k++){
            bool poly=polyCodes[j][_constraint-k-1]&&codeBuffer[k];
            out1=XOR(out1,poly);
          }
          outState1+=out1;
        }
        trellis[i][zeroOutput]=		outState0;
        trellis[i][oneOutput]=		outState1;
      }

      delete polyCodes;
      polyCodes=NULL;
      std::cout<<"Trellis Built"<<std::endl;
    }
    int CCDecoder_impl::getHammingDist(uint8_t byte_0,uint8_t byte_1){
      int hamming=0;
      for( int i=0;i<8;i++){
          hamming+=XOR(getBit(byte_0,i),getBit(byte_1,i));
      }
      return hamming;
    }
    bool CCDecoder_impl::getBit(unsigned char byte, int position)    {
        return (byte >> position) & 0x1;
    }
    bool CCDecoder_impl::XOR(bool A, bool B){
      return A!=B	;
    }
    void CCDecoder_impl::BytesToBool(const uint8_t* oldBuff,bool* newBuff,size_t length){
      size_t offset=0;
      for(size_t i=0;i<length;i++){
        for(auto j=7;j>-1;j--){
          *(newBuff+offset)=getBit(*(oldBuff+i),j);	
          offset++;
        }	

      }
    }
    void CCDecoder_impl::BoolToBytes(bool* oldBuff,uint8_t* newBuff,size_t length){
      size_t offset=0;
      for(size_t i=0;i<length;i++){
        for(int j=0;j<8;j++){
              *(newBuff+i)*=2;
          *(newBuff+i)+=*(oldBuff+offset);
          offset++;		

        }
      }
    }

  } /* namespace Custom */
} /* namespace gr */

