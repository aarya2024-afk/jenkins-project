import pytest
from app import sum_list, count_negatives

# Test sum_list against four distinct input cases
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 6),          
    ([-1, -2, -3], -6),      
    ([1.5, 2.5, -1], 3.0),   
    ([], 0)                  
])
def test_sum_list(numbers, expected):
    assert sum_list(numbers) == expected


# # Test count_negatives against three distinct input cases
@pytest.mark.parametrize("numbers, expected", [
    ([1, -2, -3, 4], 99),     # ❌ CHANGED FROM 2 TO 99 (INTENTIONAL FAILURE)
    ([1, 2, 3, 4], 0),       
    ([-5, -10, -15], 3)      
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected
