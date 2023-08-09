bool solution(int a, int b) {
    
    if(a == b){
        return false;
    }
    
    if((a+1 > b-1)){
        return true;
    }else{
        if(((a % 2 != 0) && (b % 2 == 0)) || ((a % 2 == 0) && (b % 2 != 0))){
            return true;
        }
        else{
            return false;
        }
    }
}