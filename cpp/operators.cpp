#include <iostream>
using namespace  std;
//Arithmetic Operators
int main() {
    int a = 10, b = 20;
    cout<<"the value of a is: "<<a<<endl;
    cout<<"the value of b is: "<<b<<endl;
    cout<<"the sum of a and b is: "<<(a+b)<<endl;
    cout<<"the difference of a and b is: "<<(a-b)<<endl;
    cout<<"the product of a and b is: "<<(a*b)<<endl;
    cout<<"the quotient of a and b is: "<<(a/b)<<endl;
    cout<<"the remainder of a and b is: "<<(a%b)<<endl;
    cout<<"the value of a after increment is: "<<(++a)<<endl;
    cout<<"the value of b after decrement is: "<<(--b)<<endl;
    cout<<"the value of a after post increment is: "<<(a++)<<endl;
    cout<<"the value of b after post decrement is: "<<(b--)<<endl;
    cout<<"the value of a after post increment is: "<<(a)<<endl;
    cout<<"the value of b after post decrement is: "<<(b)<<endl;

    cout << "Hello, World!";
//Relational Operatorss
    cout << "the value of a is: " << a << endl;
    cout << "the value of b is: " << b << endl;
    cout<< "the value of a==b is: " << (a==b) << endl;
    cout<< "the value of a!=b is: " << (a!=b) << endl;
    cout<< "the value of a>b is: " << (a>b) << endl;
    cout<< "the value of a<b is: " << (a<b) << endl;
    cout<< "the value of a>=b is: " << (a>=b) << endl;
    cout<< "the value of a<=b is: " << (a<=b) << endl;
//logical operators
    cout<< "the value of logical and operator is: " << ((a==b) && (a<b)) << endl;
    cout<< "the value of logical or operator is: " << ((a==b) || (a<b)) << endl;
    cout<< "the value of logical not operator is: " << (!(a==b)) << endl;

    return 0;
}