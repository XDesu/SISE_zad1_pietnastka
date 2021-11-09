def eq_2d_array(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Arrays are not the same size")
    for i in range(len(arr1)):
        if len(arr1[i]) != len(arr2[i]):
            raise Exception("Arrays are not the same size")
        for j in range(len(arr1[i])):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True
