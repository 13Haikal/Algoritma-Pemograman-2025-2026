#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <iomanip> 

using namespace std;

void hitungNIMArray() {
    string nimStr;
    cout << "Masukkan NIM: ";
    cin >> nimStr;

    vector<int> digit;
    for (char c : nimStr) {
     
        digit.push_back(c - '0'); 
    }

    
    cout << "Digit Array: [";
    for (size_t i = 0; i < digit.size(); ++i) {
        cout << digit[i] << (i < digit.size() - 1 ? ", " : "");
    }
    cout << "]" << endl;

    
    int total = accumulate(digit.begin(), digit.end(), 0);


    int maks = *max_element(digit.begin(), digit.end());
    int minim = *min_element(digit.begin(), digit.end());

    
    double rata = (double)total / digit.size();


    vector<int> rev = digit; 
    reverse(rev.begin(), rev.end()); 

   
    cout << "Total: " << total << endl;
    cout << "Maksimum: " << maks << endl;
    cout << "Minimum: " << minim << endl;
    cout << fixed << setprecision(2) << "Rata-rata: " << rata << endl; 

  
    cout << "Reverse Array: [";
    for (size_t i = 0; i < rev.size(); ++i) {
        cout << rev[i] << (i < rev.size() - 1 ? ", " : "");
    }
    cout << "]" << endl;
}

int main() {
    hitungNIMArray();
    return 0;
}