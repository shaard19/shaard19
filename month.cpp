#include <iostream>
#include <string>
using namespace std;
int main()
{
//Assaignment two section  3
int month;
cout<<"Enter a number from 1-12.";
if (month ==1)
    cout<<"January";
else if (month==2)
    cout<< "February";
else if (month==3)
    cout<<"March";
else if (month==4)
    cout<<"April";
else if (month==5)
    cout<<"May";
else if (month==6)
    cout<<"June";
else if (month==7)
    cout<<"July";
else if (month==8)
    cout<<"August";
else if (month==9)
    cout<<"September";
else if (month==10)
    cout<<"October";
else if (month==11)
    cout<<"November";
else if (month==12)
    cout<<"December";
else if (month>12)
    cout<<"Sorry I need a number from 1-12."<<endl;          
else if(month<=12) 
    cout<< "The month is "<<month;
cin>>month;
return 0;
}