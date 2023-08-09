int solution(int min1, int min2_10, int min11, int s) {
    
    int i = 0;
    
    if(s < min1){return 0;}
    if(s == min1){i++; return 1;}
    
    i++;
    s = s - min1;
    
    if (s >= (9 * min2_10)){
        i = i + 9;
        s = s - (9 * min2_10);
    }else{
        i = i + (s / min2_10);
        s = s - (i * min2_10);
    }
    
    if (s >= min11){
        i = i + (s / min11);
    }
    
    return i;
}