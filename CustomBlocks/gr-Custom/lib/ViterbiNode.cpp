//#include "ViterbiNode.h"
class ViterbiNode{
public: 	
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
	~ViterbiNode::ViterbiNode(){}
};