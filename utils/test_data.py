class TestData:
    url = "https://www.demo.guru99.com/V4/"
    titlelogin = "Guru99 Bank Manager HomePage"

    @staticmethod
    def login_credentials():
        return [
            ("mngr559247", "AjebyrU"),
            ("invalid", "AjebyrU"),
            ("mngr559247", "invalid"),
            ("invalid", "invalid")  
        ]