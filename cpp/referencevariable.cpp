#include <iostream>
using namespace std;

int c = 45;

int main() {
    int a, b, c;

    cout << "Enter the value of a: ";
    cin >> a;

    cout << "Enter the value of b: ";
    cin >> b;

    c = a + b;

    cout << "The sum of a and b is: " << c << endl;
    cout << "The value of c is: " << ::c << endl;

    float x = 10.5;
    float &y = x;

    cout << "The value of x is: " << x << endl;
    cout << "The value of y is: " << y << endl;

    return 0;
}