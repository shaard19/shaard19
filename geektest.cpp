#include <bits/stdc++.h>
using namespace std;
void removeDupWord(string str)
{
    string word = "";
    for (auto x : str) 
    {
        if (x == ' ')
        {
            cout << word << endl;
            word = "";
        }
        else {
            word = word + x;
        }
        }
    cout << word << endl;
}  
int main()
{
    string str = "Geeks for Geeks";
    removeDupWord(str);
    return 0;
}