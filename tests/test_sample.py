# content of test_sample.py
def inc(number):
    """
    Increment
    :param number:
    :return:
    """
    return number + 1


def test_answer():
    assert inc(3) == 4
