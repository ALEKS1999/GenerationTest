import unittest
from institute import Institute
from main import Specialization


class TestAddSpec(unittest.TestCase):
    
    def test_1(self): # correct add
        sp = Specialization("ФИИТ")
        inst = Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)
        
    def test_2(self):  # correct add of two objects
        sp = Specialization('ФИИТ')
        sp1 = Specialization('ИВТ')
        inst = Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)

    def test_3(self): # incorrect add of null Spec
        sp = Specialization('')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_spec(sp)
        self.assertEqual('Specialization name is null', str(context.exception))
        self.assertEqual(len(inst.specs), 0)
        
    def test_4(self): # incorrect add of None object
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_spec(None)
        self.assertEqual('Specialization is null', str(context.exception))
        self.assertEqual(len(inst.specs), 0)
        
    def test_5(self): # incorrect add: existing object
        sp = Specialization('ФИИТ')
        sp1 = Specialization('ФИИТ')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_spec(sp)
            inst.add_spec(sp1)
        self.assertEqual('Specialization already exist', str(context.exception))
        self.assertEqual(len(inst.specs), 1)
        
    def test_6(self): # incorrect add(Wrong type)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_spec(1)
        self.assertEqual('Wrong type', str(context.exception))
        self.assertEqual(len(inst.specs), 0)
    


class TestGetSpec(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls._spec = Specialization("ФИИТ")
        cls._inst = Institute()
        cls._inst.add_spec(cls._spec)
    
    def test_1(self): # correct get
        get_spec = self._inst.get_spec("ФИИТ")
        self.assertEqual(type(get_spec), Specialization)
        self.assertEqual(get_spec, self._spec)
        
    def test_2(self): # incorrect get(Wrong type)
        with self.assertRaises(Exception) as context:
            get_spec = self._inst.get_spec(1)
        self.assertEqual("Wrong type", str(context.exception))
        
    def test_3(self): # incorrect get(Name is null)
        with self.assertRaises(Exception) as context:
            get_spec = self._inst.get_spec('')
        self.assertEqual("Name is null", str(context.exception))