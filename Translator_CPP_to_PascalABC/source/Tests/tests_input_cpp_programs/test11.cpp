int megafunc(int a, int b, int c) {
 if (a > 5)
 {
    a = 4 * a;
 }
 else
 {
    if (b < 3)
    {
        b = 2 * c;
    }
    else
    {
        c = b * a * 6;
    }
 }
 return 3;
}

void main() {
    int a = 3;
    int b = 2;
    int c = megafunc(a,b,5);
    std::cout << c;
}