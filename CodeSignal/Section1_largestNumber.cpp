int solution(int n) {

    int total = 1;
    for(int i = 1; i <= n; i++){
        total = 10 * total;
    }
    
    return total - 1;
}