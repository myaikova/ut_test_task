

def test_increase_counter(app):
    counter_start = app.counter_helper.check_counter()
    app.counter_helper.increase()
    assert not app.counter_helper.is_invalid(), 'Counter val is "Invalid", expected %s' % (int(counter_start) + 1)
    counter_finish = app.counter_helper.get_val()
    assert int(counter_finish) == int(counter_start) + 1


def test_increase_multiple_times(app):
    counter_start = app.counter_helper.check_counter()
    for i in range(20):
        app.counter_helper.increase()
        assert not app.counter_helper.is_invalid(), 'Counter val is "Invalid", expected %s' % (int(counter_start) + 1)
        counter_finish = app.counter_helper.get_val()
        assert int(counter_finish) == int(counter_start) + i + 1


def test_reload_page(app):
    counter_start = app.counter_helper.check_counter()
    app.counter_helper.increase()
    app.my_helper.reload_page()
    assert not app.counter_helper.is_invalid(), 'Counter val is "Invalid", expected %s' % (int(counter_start) + 1)
    counter_finish = app.counter_helper.get_val()
    assert int(counter_finish) == int(counter_start) + 1


def test_counter_after_relogin(app):
    counter_start = app.counter_helper.check_counter()
    app.counter_helper.increase()
    app.my_helper.logout()
    app.my_helper.login()
    assert not app.counter_helper.is_invalid(), 'Counter val is "Invalid", expected %s' % (int(counter_start) + 1)
    counter_finish = app.counter_helper.get_val()
    assert int(counter_finish) == int(counter_start) + 1
