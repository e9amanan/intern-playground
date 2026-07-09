import pytest
from week1day2.utils.text import clean_text,tokenize,count_chars

def test_clean_text_happy_path():
    assert clean_text(" HEllo, WORLd!  ") == "hello, world!"

def test_clean_text_edge_cases():
    assert clean_text("") == ""
    assert clean_text("    ") == ""
    assert clean_text("HEllo  woRLd       HoW") == "hello world how"

def test_tokenize_custom_delimiter():
    assert tokenize("apple,banana,orange",delimiter=",") == ["apple","banana","orange"]

def test_tokenize_happy_path():
    assert tokenize("hello world") == ["hello", "world"]

def test_tokenize_edge_case():
    assert tokenize("") == [""]

def test_count_chars_happy_path():
    assert count_chars("hello")=={"h":1,"e":1,"l":2,"o":1}

def test_count_chars_edge_case():
    assert count_chars("")=={}

def test_tokenize_edge_case1():
    assert tokenize("123",delimiter=",")==["123"]

def test_tokenize_invalid_type_integer():
    with pytest.raises(AttributeError):
        tokenize(123)

def test_tokenize_invalid_type_none():
    with pytest.raises(AttributeError):
        tokenize(None)



