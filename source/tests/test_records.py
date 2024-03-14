import pytest
from addressbook.records import Record

def test_record():
    """ Simple testcases """
    record = Record.from_json(
            {
                "phones": ['1234567890', '0987654321'],
                "emails": ['test_1@goit.com', 'test2@goit.com'],
                "address": "test test test",
                "birthday": "03.04.1995"
            }
        )

    assert record.read('phone') == ['1234567890', '0987654321']
    assert record.read('email') == ['test_1@goit.com', 'test2@goit.com']
    assert record.read('birthday') == "03.04.1995"
    assert record.read('address') == "test test test"

    record.add('phone', '5555555555')
    assert record.read('phone') == ['1234567890', '0987654321', '5555555555']

    with pytest.raises(ValueError):
        record.add('phone', None)
        record.add('phone', '')

    record.add('email', 'test3@goit.com')
    assert record.read('email') == ['test_1@goit.com', 'test2@goit.com', 'test3@goit.com']

    record.delete('phone', '1234567890')
    record.delete('email', 'test2@goit.com')
    assert record.read('phone') == ['0987654321', '5555555555']
    assert record.read('email') == ['test_1@goit.com', 'test3@goit.com']

    record.update('phone', '5555555555', '6666666666')
    record.update('email', 'test_1@goit.com', 'test5@goit.com')
    record.update('address', None, 'test2 test2 test2')
    record.update('birthday', None, '05.10.1995')

    assert record.read('phone') == ['0987654321', '6666666666']
    assert record.read('email') == ['test5@goit.com', 'test3@goit.com']
    assert record.read('address') == 'test2 test2 test2'
    assert record.read('birthday') == '05.10.1995'
    print("Record tests passed!")

if __name__ == "__main__":
    test_record()
