def solution(arr, delete_list):
    for delete in delete_list:
        while delete in arr:
            arr.remove(delete)
    return arr