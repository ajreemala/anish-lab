class MyArrays(object):
    def __init__(self):
        pass

    def search(self, search_array, unit):
        for num in search_array:
            if num==unit:
                return True

        return False

    def bsearch(self, search_array, num):
        left = 0
        right = len(search_array) - 1
        while left <= right:
            mid = (left + right)/2
            if search_array[mid] == num:
                return True
            if num < search_array[mid]:
                right = mid-1
            elif num > search_array[mid]:
                left = mid + 1
        return False
