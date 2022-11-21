def test_whoami():
    import libaws.whoami as whoami

    whoami.whoami()

    assert True
    