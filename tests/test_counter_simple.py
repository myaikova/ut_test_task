

def test_increase_counter(app):
    counter_start = app.counter_helper.get_val()
    counter_start != 'Invalid'
    app.counter_helper.increase()
    counter_finish = app.counter_helper.get_val()
    assert counter_finish != 'Invalid', 'Counter val is "Invalid", expected %s' % (int(counter_start)  + 1)
    assert int(counter_finish) == int(counter_start) + 1


def test_increase_multiple_times(app):
    counter_start = app.counter_helper.get_val()
    assert counter_start != 'Invalid'
    for i in range(20):
        app.counter_helper.increase()
        counter_finish = app.counter_helper.get_val()
        assert counter_finish != 'Invalid', 'Counter val is "Invalid", expected %s' % (int(counter_start) + i + 1)
        assert int(counter_finish) == int(counter_start) + i + 1


def test_reload_page(app):
    counter_start = app.counter_helper.get_val()
    assert counter_start != 'Invalid'
    app.counter_helper.increase()
    app.my_helper.reload_page()
    counter_finish = app.counter_helper.get_val()
    assert counter_finish != 'Invalid', 'Counter val is "Invalid", expected %s' % (int(counter_start) + 1)
    assert int(counter_finish) == int(counter_start) + 1