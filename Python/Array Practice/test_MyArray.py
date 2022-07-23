# ----------
# My Array Unit Testing
# 2022-07-17
# ----------
# Goals:
# - Gain experience writing and using unit tests
# - Test MyArray object class

import MyArray
    
def test_MyArrayPop():
    TestArray = MyArray.MyIntArray(0)
    TestArray.push(5)
    assert TestArray.pop() == 5