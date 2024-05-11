import database_operation as dbop


def test_unit_0():
    print(dbop.init_dolfin_db())


def test_unit_1():
    """If you want to test this function, please change the mobile number to your own"""
    print(dbop.register_user('databytes@gmail.com', '', 'Wentworth', '', '', '12345', "", "", "","","","","",""))


def test_unit_2():
    print(dbop.register_basiq_id(1))


def test_unit_3():
    print(dbop.link_bank_account(1))


def test_unit_4():
    print(dbop.cache_transactions(1, dbop.request_transactions(1)))


def test_unit_5():
    print(dbop.fetch_transactions_by_user(1))


def test_unit_6():
    print(dbop.clear_transactions())
