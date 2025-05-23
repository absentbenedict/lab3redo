print("Lab 3 - Software Unit Testing with PyTest")

# Constants for sorting order
SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    """
    Sorts the list arr using bubble sort based on sorting_order.

    Returns:
        - sorted list (if valid input and length < 10)
        - 0 if arr is empty
        - 1 if arr has 10 or more elements
        - 2 if any element is not an int
        - [] if sorting_order is invalid
    """
    arr_result = arr.copy()
    n = len(arr_result)

    # Check for empty input
    if n == 0:
        return 0  # empty input
    
    # Check for too many elements
    if n >= 10:
        return 1  # too many elements

    # Check if all elements are integers
    for s in arr_result:
        if type(s) is not int:
            return 2  # invalid element type

    # Validate sorting_order parameter
    if sorting_order not in (SORT_ASCENDING, SORT_DESCENDING):
        return []  # invalid sorting order

    # Bubble sort algorithm
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            else:  # SORT_DESCENDING
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result

def main():
    # Driver code to test the bubble_sort function
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()
