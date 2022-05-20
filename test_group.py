import unittest
from institute import Institute
from main import Specialization, Group

class TestAddGroup(unittest.TestCase):
    
    def test_1(self): # correct add(One object)
        sp = Specialization("ФИИТ")
        grp = Group("М-ФИИТ-21", 2021, sp)
        inst = Institute()
        inst.add_group(grp)
        self.assertEqual(len(inst.groups), 1)
        
    def test_2(self): # correct add(Two objects)
        sp1 = Specialization("ФИИТ")
        sp2 = Specialization("ИВТ")
        grp1 = Group("М-ФИИТ-21", 2021, sp1)
        grp2 = Group("М-ИВТ-21", 2021, sp2)
        inst = Institute()
        inst.add_group(grp1)
        inst.add_group(grp2)
        self.assertEqual(len(inst.groups), 2)
        
    def test_3(self): # incorrect add(None object)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_group(None)
        self.assertEqual("Group is null", str(context.exception))
        self.assertEqual(len(inst.groups), 0)
        
    def test_4(self): # incorrect add(Name is null)
        sp = Specialization("ФИИТ")
        grp = Group("", 2021, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_group(grp)
        self.assertEqual("Group name is null", str(context.exception))
        self.assertEqual(len(inst.groups), 0)
        
    def test_5(self): # incorrect add(Existing object)
        sp = Specialization("ФИИТ")
        grp = Group("М-ФИИТ-21", 2021, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_group(grp)
            inst.add_group(grp)
        self.assertEqual("Group already exist", str(context.exception))
        self.assertEqual(len(inst.groups), 1)
        
    def test_6(self): # incorrect add(Negative year)
        sp = Specialization("ФИИТ")
        grp = Group("М-ФИИТ-21", -2, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_group(grp)
        self.assertEqual("Group year is negative", str(context.exception))
        self.assertEqual(len(inst.groups), 0)    
        
class TestGetGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._spec = Specialization('ФИИТ')
        cls._grp = Group("М-ФИИТ-21", 2021, cls._spec)
        cls._inst = Institute()
        cls._inst.add_group(cls._grp)
        
    def test_1(self): # correct get
        get_group = self._inst.get_group("М-ФИИТ-21")
        self.assertEqual(type(get_group), Group)
        self.assertEqual(get_group, self._grp)