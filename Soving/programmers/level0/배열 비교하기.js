function solution(arr1, arr2) {
    const sum1 = arr1.reduce((acc, val) => acc + val, 0);
    const sum2 = arr2.reduce((acc, val) => acc + val, 0);

    if (arr1.length < arr2.length ) {
        return -1;
    } else if (arr1.length > arr2.length) {
        return 1;
    } else if (sum1 > sum2) {
        return 1;
    } else if (sum1 < sum2) {
        return -1;
    }
    return 0;
}