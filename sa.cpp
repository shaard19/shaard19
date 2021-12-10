#include <iostream>
using namespace std;

int main()
{
    int k, i;

    for(k = 1; k <= 5; k++)
	{
        cout << k << ". Outer loop\n";

        for(i = 0; i < 10; i+2)
		{
            cout << "\t"<< i << ". Inner loop\n";
        }
    }
    return 0;
}