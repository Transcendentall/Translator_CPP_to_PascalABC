void main() {
    int a = 4;
    int i = 1;
    int j = 1;
    for (i = 1; i < 10; i++)
    {
        for (j = 10; j > 5; j--)
        {
            a = a + i - j;
        }
    }
    std::cout << a;
}
