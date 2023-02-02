int cou(int a) {
while (a < 100)
{
    a = a * a - a + a * 3 - 4;
    std::cout << a;
}
    return a;
}

void main() {
    int a = 7;
    a = cou(a);
}