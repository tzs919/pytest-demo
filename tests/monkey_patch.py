import tests.app as app


def test_connection(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIG, "user", "test_user")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "database", "test_db")

    expected = "User Id=test_user; Location=test_db;"
    result = app.create_connection_string()
    assert result == expected
