function solution(n) {
    var answer = 0;
    if (n%2===1) {
        for(i=1; i<n+1; i++) {
            if (i%2===1) {
                answer += i;
            }
        }
        return answer;
    }
    for(i=1; i<n+1; i++) {
        if (i%2===0) {
            answer += i*i;
        }
    }
    return answer;
}