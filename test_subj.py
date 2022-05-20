from institute import Institute
from main import Subject, Specialization
import unittest

class TestAddSubj(unittest.TestCase):
    
    def test_1(self): # correct add(one object)
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', 1, 172, sp)
        inst = Institute()
        inst.add_subject(subj)
        self.assertEqual(len(inst.subjects), 1)
        
    def test_2(self): #correct add(two objects)
        sp1 = Specialization("ФИИТ")
        sp2 = Specialization("ИВТ")
        subj1 = Subject('Б1', 'Основы программирования', 1, 172, sp1)
        subj2 = Subject('Б1', 'Основы программирования', 1, 144, sp2)
        inst = Institute()
        inst.add_subject(subj1)
        inst.add_subject(subj2)
        self.assertEqual(len(inst.subjects), 2)
    
    def test_3(self): #incorrect add(None object)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(None)
        self.assertEqual('Subject is null', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
        
    def test_4(self): #incorrect add(Existing object)
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', 1, 172, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(subj)
            inst.add_subject(subj)
        self.assertEqual('Subject already exist', str(context.exception))
        self.assertEqual(len(inst.subjects), 1)
        
    def test_5(self): # incorrect add(Name is null)
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', '', 1, 172, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(subj)
        self.assertEqual('Subject name is null', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
        
    def test_6(self): # incorrect add(code is null)
        sp = Specialization("ФИИТ")
        subj = Subject('', 'Основы программирования', 1, 172, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(subj)
        self.assertEqual('Subject code is null', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
        
    def test_7(self): # incorrect add(semester is negative)
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', -1, 172, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(subj)
        self.assertEqual('Subject semester can not be negative', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
        
    def test_8(self): # incorrect add(code is null)
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', 1, -3, sp)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(subj)
        self.assertEqual('Subject hour can not be negative', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
        
    def test_9(self): # incorrect add(wrong type)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_subject(1)
        self.assertEqual('Wrong type', str(context.exception))
        self.assertEqual(len(inst.subjects), 0)
    
class TestGetSubj(unittest.TestCase):    
    
    def test_1(self):
        pass