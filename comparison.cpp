#include<iostream>
using namespace std;
int main()
{
	//Assaignment two section  1
    char str1[50], str2[50];
    int i=0, chk=0;
    cout<<"Enter the First String: ";
    cin>>str1;
    cout<<"Enter the Second String: ";
    cin>>str2;
    while(str1[i]!='\0' || str2[i]!='\0')
    {
        if(str1[i]!=str2[i])
        {
            chk = 1;
            break;
        }
        i++;
    }
    if(chk==0)
        cout<<"\nStrings are Equal";
    else
        cout<<"\nStrings are not Equal";
    cout<<endl;
    return 0;
}