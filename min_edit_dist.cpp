#include<iostream>
#include<string>
using namespace std;
int min(int x, int y, int z)
{
    //making a new min function because the one in cpp has only two args
    return min(min(x,y),z);
}

int min_ed(std::string s1, std::string s2, int l1, int l2)
{
    if(l1==0)
        return l2;
    
    if(l2==0)
        return l1;

    if(s1[l1-1]==s2[l2-1])
        return min_ed(s1,s2,l1-1,l2-1);
    
    return 1+min(min_ed(s1,s2,l1,l2-1),//insert
                 min_ed(s1,s2,l1-1,l2),//remove
                 min_ed(s1,s2,l1-1,l2-1)//delete
                );       
}

int main()
{
    std::string s1="saturday";
    std::string s2="sunday";
    int minEd=min_ed(s1,s2,s1.length(),s2.length());
    std::cout<<minEd;
    return 0;
}
