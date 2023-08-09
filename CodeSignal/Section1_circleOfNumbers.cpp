int solution(int n, int firstNumber) {
    
	int halfway = firstNumber + (n / 2);
    
	if (halfway >= n){
        return halfway - n;
    }
    
	return halfway;
}