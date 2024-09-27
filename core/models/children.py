
class Children:
    _uid = None
    _children = []

    # TODO: implement this class model

    # INIT
    def __init__(self, uid, children = []):
        self.uid = uid
        self._children = children

    # returns the uid of the children
    def get_id(self):
        return self.uid