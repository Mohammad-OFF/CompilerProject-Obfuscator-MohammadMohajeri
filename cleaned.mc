int multiply(int param1) {
    int var1 = param1 * 2;
    if (param1 > 5) {
        var1 = var1 + 10;
        int var2 = 100;
        var1 = var1 - (var2 / 10);
    }
    else {
        var1 = var1 - 1;
    }
    return var1;
}

int main() {
    int var1 = 7;
    int var2 = multiply(var1);
    printf("Result: %d\n", var2);
    var1 = 0;
    while (var1 < 2) {
        int var3 = var1 + 1;
        printf("Looping: %d\n", var3);
        var1 = var1 + 1;
    }
    return 0;
}
