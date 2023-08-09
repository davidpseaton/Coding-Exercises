int solution(int n, int m) {
    
    int total = 0;
    
    if (m >= n){
        int initDiv = m / n;
        total = n * initDiv;
    }

    return total;
}