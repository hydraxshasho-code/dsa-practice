//Inline Functions, Default Arguments & Constant Arguments in C++ | C++ Tutorials for Beginners #17


#include <iostream>
using namespace std;

inline int product(int a, int b) {
    return a * b;
}
int main() {
    cout << "This is main function" << endl;
    int a, b;
    cout << "Enter two numbers:\n";
    cin >> a >> b;
    cout<<"product of two numbers: "<<product(a,b)<<endl;
    return 0;
}