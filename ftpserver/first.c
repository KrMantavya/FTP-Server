#include<iostream.h>
#include<iomanip.h>
main()
{
int x;
float y;
cin>>x;
cin>>y;
if(x>0 && x<=2000)
 if(y>0 && y<=2000)
  if(x%5==0)
   if(x<y)
     {
       y=y-x-0.50;
     }
cout<< std::fixed;
cout<<std::setprecision(2) <<y;
}
