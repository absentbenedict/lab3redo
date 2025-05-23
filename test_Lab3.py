import Lab3  # adjust if your Lab3.py is in a module/folder

def test_bubble_sort_ascending():
    # REQ-01: <10 numbers, SORT_ASCENDING returns ascending sorted list
    input_arr = [5, 3, 8, 1]
    expected = [1, 3, 5, 8]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected

def test_bubble_sort_descending():
    # REQ-02: <10 numbers, SORT_DESCENDING returns descending sorted list
    input_arr = [5, 3, 8, 1]
    expected = [8, 5, 3, 1]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == expected

def test_bubble_sort_too_many():
    # REQ-03: >= 10 numbers returns 1
    input_arr = list(range(10))  # 10 numbers
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1

def test_bubble_sort_empty():
    # REQ-04: 0 numbers returns 0
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0

def test_bubble_sort_invalid_input():
    # REQ-05: non-integers return 2
    input_arr = [1, 2, 'a', 4]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2
