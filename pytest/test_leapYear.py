import pytest
import leapYear

inp1 = 2000
inp2 = 100
inp3 = 1999
inp4 = "2000"


def test_inputType1():
    assert type(inp1)==type(123)
def test_inputType2():
    assert type(inp2)==type(123)
def test_inputType3():
    assert type(inp3)==type(123)
def test_inputType4():
    assert type(inp4)==type(123)

def test_returnType1():
    result = leapYear.isLeapYear(inp1)
    assert type(result)==type(True)
def test_returnType2():
    result = leapYear.isLeapYear(inp2)
    assert type(result)==type(True)
def test_returnType3():
    result = leapYear.isLeapYear(inp3)
    assert type(result)==type(True)
def test_returnType4():
    result = leapYear.isLeapYear(inp4)
    assert type(result)==type(True)

def test_correctResult1():
    result = leapYear.isLeapYear(inp1)
    correct_result = True
    assert result==correct_result
def test_correctResult2():
    result = leapYear.isLeapYear(inp2)
    correct_result = False
    assert result==correct_result
def test_correctResult3():
    result = leapYear.isLeapYear(inp3)
    correct_result = False
    assert result==correct_result
def test_correctResult4():
    result = leapYear.isLeapYear(inp4)
    correct_result = False
    assert result==correct_result
