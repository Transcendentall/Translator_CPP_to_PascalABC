int super_calculator(int n) {
    int b = n + 2;
    int calc = 0;
    b = b * 2;
    if (b < 10)
    {
        calc = b - 4;
    }
    else
    {
        if (b > 20)
        {
            calc = b * b;
        }
        else
        {
            std::cout << 00000000000000000000;
            calc = 2;
        }
    }
    return calc;
}

void main() {
    int a = 3;
    int r = 0;
    r = super_calculator(a);
    std::cout << r;
}
