int solution(int value1, int weight1, int value2, int weight2, int maxW) {

    if (weight1 + weight2 <= maxW){
        return value1 + value2;
    }
    
    if (weight1 <= maxW || weight2 <= maxW){
        
        if (weight1 <= maxW && weight2 > maxW){
            return value1;
        }
        else if (weight2 <= maxW && weight1 > maxW){
            return value2;
        }
        else {
            if (value1 > value2){
                return value1;
            }
            if (value2 > value1){
                return value2;
            }
            return value1;
        }
    }
    return 0;
}