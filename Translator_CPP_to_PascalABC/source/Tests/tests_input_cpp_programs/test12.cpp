int super_calculator(int n) {
    int b = n + 2;
    int calc = 0;
    b = b * 2;
    if (b < 10)
    {
        int u = 3;
        calc = u;
        calc = b - 4;
    }
    else
    {
        if (b > 20)
        {
            int u = 6;
            calc = b * b;
        }
        else
        {
            std::cout << 00000000000000000000;
            calc = 2;
            if (b == 15)
            {
                int u = 9;
                while (b > 12)
                {
                    calc++;
                    calc = calc + u;
                    b--;
                }
            }
        }
    }
    return calc;
}

void main() {
    int a = 3;
    if (a == 3)
    {
        int r = 5;
        r = super_calculator(a);
        std::cout << r;
    }
}