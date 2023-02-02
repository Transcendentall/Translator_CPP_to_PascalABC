int func1(int x, int y) {
    return x + y;
}

int func2(int x, int y, int z) {
    return x * y * z;
}

void main() {
    int a = 3;
    int b = 2;
    int r = 0;
    r = func2(func1(a,r),b,a);
    std::cout << r;
}