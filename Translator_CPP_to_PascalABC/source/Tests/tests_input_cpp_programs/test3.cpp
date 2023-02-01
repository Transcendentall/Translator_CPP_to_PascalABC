void main() {
    int a = 2;
    int b = 2;
    int c = 2 + a + b - 5 * 2 + 1 - a * b + 4;
    if (c > 3)
    {
        c = c + b;
    }
    std::cout << c;
}