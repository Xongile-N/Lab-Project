#include <vector>
#include <math.h>
#include <stdlib.h> 
#include <complex>
#include <cstring> 
#include <algorithm>
class ViterbiNode{
    public:
        ViterbiNode();
	    ViterbiNode(int);
	    void addPath(const std::vector<int> , int);
        int getPathHamming();
        int getPrevPathHamming();
        int getPrevPrevPathHamming();
        int getPathLength();
        int getPrevPathLength();
        int getPrevPrevPathLength();
        std::vector<int> getPath();
        std::vector<int> getPrevPath();
        std::vector<int> getPrevPrevPath();
	    void deletePath();
	~ViterbiNode();
    private:
        int pathHamming=1000000;	
        int prevPathHamming=1000000;
        int prevPrevPathHamming=1000000;

        std::vector<int> path;	
        std::vector<int> prevPath;
        std::vector<int> prevPrevPath;
        int trellisIndex=0;
        bool nodeAlloc=false;
};