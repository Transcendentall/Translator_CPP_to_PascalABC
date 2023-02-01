int func1(int x) {
    return 1;
}

int func2(int y) {
    return y + 2 + 3;
}

int func3(int z) {
    z = 2 + 3 - z;
    return z - 4 + 1 * 5;
}

void main() {
    int a = 3;
    int r = 0;
    r = func3(func2(func1(a)));
    std::cout << r;
}
