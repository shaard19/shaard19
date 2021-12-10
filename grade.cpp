#include<iostream>
using namespace std;
int main()
{
	//Assaignment two section 2
    int marks;
    cout<<"Enter Marks obtained by the student";
    {
        cin>>marks;
    }
    if(marks>=60)
        cout<<"Congratulations, you have passed";
    else if(marks<=60)
        cout<<"Sorry, you failed";
    else
        cout<<"Invalid!";
    cout<<endl;
    return 0;
}