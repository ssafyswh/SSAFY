#include <stdio.h>

int f(int n) {
    if (n == 0) return 1;
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += f(i);
    return sum % 13;
}

int main() {
    char ans[] = "rgjgmbuyhbfcx";
    for (int i = 0; i < 13; i++) 
        ans[i] ^= f(13 + i * i * i);
    puts(ans);
}