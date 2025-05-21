// input.mc
int calculate(int val) {
    int result = val * 2;
    if (val > 5) {
        result = result + 10;
        int temp = 100; // Statement
        result = result - temp / 10; // Statement
    } else {
        result = result - 1; // Statement
    }
    return result;
}

int main() {
    int x = 7;
    int y;
    y = calculate(x); // Statement
    printf("Result: %d\n", y); // Statement
    x = 0; // Statement
    while (x < 2) {
        int inner_val = x + 1; // Statement in a block
        printf("Looping: %d\n", inner_val); // Statement in a block
        x = x + 1; // Statement in a block
    }
    return 0;
}