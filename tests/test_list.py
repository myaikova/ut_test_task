import random
import pytest
from test_data.list import records, incorrect_records


@pytest.mark.parametrize('record', records)
def test_correct_record(app, record):
    app.list_helper.insure_place_available()
    old_list = app.list_helper.get_record_list()
    app.list_helper.add_record(record)
    new_list = app.list_helper.get_record_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(record)
    assert old_list == new_list


def test_delete_record(app):
    app.list_helper.insure_record_exists()
    old_list = app.list_helper.get_record_list()
    num = random.choice(range(0, len(old_list)))
    app.list_helper.remove_record(num)
    new_list = app.list_helper.get_record_list()
    assert len(old_list) == len(new_list) + 1
    old_list[num: num + 1] = []
    assert old_list == new_list
    pass


def test_add_max_records_num(app):
    if len(app.list_helper.get_record_list()) == app.list_helper.max_list_len:
        assert True
    else:
        for i in range(app.list_helper.max_list_len - len(app.list_helper.get_record_list()) - 1):
            app.list_helper.add_record('lalala')
        old_list = app.list_helper.get_record_list()
        app.list_helper.add_record('lalala')
        new_list = app.list_helper.get_record_list()
        assert len(old_list) + 1 == len(new_list)
        old_list.append('lalala')
        assert old_list == new_list


def test_eleven_records(app):
    if len(app.list_helper.get_record_list()) < app.list_helper.max_list_len:
        for i in range(app.list_helper.max_list_len - len(app.list_helper.get_record_list())):
            app.list_helper.add_record('lalala')
    old_list = app.list_helper.get_record_list()
    app.list_helper.add_record('lalala')
    new_list = app.list_helper.get_record_list()
    assert len(old_list) == len(new_list)
    assert old_list == new_list
    assert app.my_helper.warning_shown()


@pytest.mark.parametrize('record', incorrect_records)
def test_incorrect_record_len(app, record):
    app.list_helper.insure_place_available()
    old_list = app.list_helper.get_record_list()
    app.list_helper.add_record(record)
    new_list = app.list_helper.get_record_list()
    assert old_list == new_list
    assert app.my_helper.error_shown()

