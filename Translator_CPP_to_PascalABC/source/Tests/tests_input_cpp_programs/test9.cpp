int fun1(int n) {
    int b = n + 2;
    int f = 0;
    b = b * 2;
    if (b < 10)
    {
        f = b - 4;
    }
    else
    {
        if (b > 20)
        {
            f = b * b;
        }
        else
        {
            std::cout << 00000000000000000000;
            f = 2;
        }
    }
    return f;
}

void main() {
    int a = 3;
    int b = 0;
    b = fun1(a);
    std::cout << b;
}
