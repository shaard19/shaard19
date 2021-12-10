#include <iostream>
using namespace std;

int main()
 {
    int number;
    int sum ;
    cout << "Enter a number: ";
    cin >> number;

    for (int i =0;  i =10;)
	{
        sum += number;
        cout << "Enter a number: ";
        cin >> number;
    }

    cout << "The sum is " << sum << endl;
    
    return 0;
}