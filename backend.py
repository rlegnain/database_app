
import collections



class onImp:
    def on_delete(self): pass
    def on_change(self): pass
    def on_add(self): pass




class person(collections.UserDict):

    def __init__(self):
        super().__init__()
        self.data = {}

    def ask_change(self, key, value):
        """ Changes the value"""
        if self.get(key, None) is None:
            raise KeyError
        self.data[key] = value


class Woman(person):
    """
    This class is inherited from collections.UserDict. Each instance
    object of this has all the information needed for each female person.
    """
    def __init__(self):
        person.__init__()
        # +============================================================+
        # |               Required information                         |
        # +============================================================+
        self.data['family id'] = None
        self.data['first name'] = ''
        self.data['last name'] = ''
        self.data['data of birth'] = ''
        self.data['study level'] = ''
        self.data['address'] = ''
        self.data['phone number'] = ''
        self.data['marital status'] = ''
        self.data['health status'] = ''
        self.data['occupation'] = ''
        self.data['need training'] = False  # dose she need a job
        self.data['reason'] = ''  # why she need a job
        self.data['training'] = ''  # kind of training
        self.data['need transportation'] = ''  # dose she need a transportation
        self.data['available time'] = ''  # dose she need a transportation
        self.data['income'] = ''
        self.data['number of children'] = 0
        # self.data['children'] = {}


class Child(person):

    def __init__(self):
        person.__init__()
        # +============================================================+
        # |               Required information                         |
        # +============================================================+
        self.data['family id'] = None
        self.data['first name'] = ''
        self.data['last name'] = ''
        self.data['data of birth'] = ''
        self.data['study level'] = ''
        self.data['grad last year'] = ''
        self.data['need tutor'] = False
        self.data['courses'] = []
        self.data['need transportation'] = ''  # dose need a transportation
        self.data['hobbies'] = ''


class Myfile(collections.UserDict):

    def __init__(self, controller):
        super.__init__()
        self.controller = controller
        self.data['woman'] = {}  # woman is dict={familyID:womanInfo,}
        self.data['child'] = {}  # child is dict={familyId:childInfo}


    def ask_addWoman(self, info={}):
        """Adds new woman entry"""
        # generate new familyID
        familyID = self._generate_familyID()
        self.data['woman'][familyID] = info

        self.controller.on_add()


    def ask_addChild(self, familyID = None, info={}):
        """Adds new child entry"""
        if familyID is None:
            raise TypeError("backend-ask_addChild(): familyID params must not be none")
        self.data['child'][familyID] = info


    def _generate_familyID(self):
        """ Generates a new family id. A new family id is the last family-id+1"""
        return max(self.data['woman'].keys()) + 1

    def ask_deleteWoman(self, familyID=None):
        if familyID is None:
            raise TypeError("backend-ask_delete(): familyID params must not be none")
        if self['woman'].get(familyID, None) is None:
            raise TypeError("backend-ask_delete(): familyID is not exist".format(familyID))
        # delete this woman object
        del self.data['woman'][familyID]
        # delete all children belong to this familyID
        for n in self.data['child']:
            if n == familyID:

    def ask_change(self, infoDict):
        """Changes information in"""


    def ask_get(self):
        pass
