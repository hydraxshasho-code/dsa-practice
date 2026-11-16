//Constants, Manipulators & Operator Precedence | C++ Tutorials for Beginners #8 code with harry

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a = 10;
    cout << "The value of 1st variable is " << a << endl;
    a=45;
    cout << "The value of 1st variable is now " << a << endl;
//here we checked that value can be updated and changed just like in python but in python. 
//now constants 
     const int b = 20;
     cout << "The value of 2nd variable is " << b << endl;
     //b= 45; //this will give an error because we cannot change the value of a constant variable
     //cout << "The value of 2nd variable is now " << b << endl;
     int x = 45, y = 78;
     cout << "The value of x without setw is " << x << " and the value of y without setw is " << y << endl;
     cout<< "The value of x with setw is " << setw(199) << x <<endl;
     cout<< "The value of y with setw is " << setw(4) << y <<endl;  
     //so basically setw is used to set the width of the output field. It is used to format the output. It is used to align the output in a tabular format. It is used to set the width of the output field. It is used to format the output. It is used to align the output in a tabular format.
     //Operator precedence is
     int m= 3, n=4;
        cout << "The value of m+n*5 is " << m+n*5 << endl; // here * has higher precedence than + so it will be evaluated first

    return 0;

}
