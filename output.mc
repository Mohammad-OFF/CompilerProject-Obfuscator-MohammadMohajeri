int obf_1(int obf_2) {
    int obf_3 = obf_2 * 2;
    if (obf_2 > 5) {
        obf_3 = obf_3 + 10;
        int obf_4 = 100;
        obf_3 = obf_3 - (obf_4 / 10);
    }
    else {
        obf_3 = obf_3 - 1;
    }
    int obf_1 = 2231;
    return obf_3;
}

int main() {
    int obf_5 = 7;
    int obf_6;
    obf_6 = obf_1(obf_5);
    printf("Result: %d\n", obf_6);
    int obf_2 = 880;
    obf_5 = 0;
    while (obf_5 < 2) {
        int obf_7 = obf_5 + 1;
        printf("Looping: %d\n", obf_7);
        obf_5 = obf_5 + 1;
    }
    return 0;
}
