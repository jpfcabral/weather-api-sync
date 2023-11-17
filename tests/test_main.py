from app.main import status_check


class TestMain:
    def test_setup(self):
        result = status_check()

        assert result == {"status": "ok"}
