int solution(int n) {

    int hour = n / 60;
    int minute = n - (hour * 60);

    stringstream ss;
    ss << hour << minute;
    string numstr = ss.str();

    int total = 0;
    int i = 0;
    int tempI = 0;
    char tempC = 'c';
    
    for(i = 0; numstr[i] != '\0'; i++){
        tempC = numstr[i];
        tempI = tempC - '0';
        total = total + tempI; 
    }
  
    return total;
}