int solution(int n) {
    
    stringstream ss;
    ss << n;
    string numstr = ss.str();
    
    char first = numstr[0];
    char second = numstr[1];
    
    int num1 = first - '0';
    int num2 = second - '0';

    int total = num1 + num2;

    return total;
}