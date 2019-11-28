def test_diff_func(func):
    assert func(0, 190) == 170, 'FAIL'
    assert func(0, 180) == 180, 'FAIL'
    assert func(0, 45) == 45, 'FAIL'
    assert func(120, 280) == 160, 'FAIL'


def diff(x, y):
    dif = abs(x - y)
    if dif > 180:
        dif = 360 - dif
    return dif


test_diff_func(diff)