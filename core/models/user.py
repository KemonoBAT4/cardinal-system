
class User:

    _user_id = 0
    _username = ""
    _user_email = ""
    _user_name = ""
    _user_surname = ""

    # TODO: implement this class model

    def __init__(self, username = "", user_email = "", name = "", surname = ""):
        
        self._username = username
        self._user_email = user_email
        self._user_name = name
        self._user_surname = surname
    #enddef

    # TODO: implement this functions
    def _check_user(user_email):
        return False
    #enddef

    def add_user(self):
        pass
    #enddef

    def delete_user(self):
        pass
    #enddef

    def update_user(self):
        pass
    #enddef
#endclass
