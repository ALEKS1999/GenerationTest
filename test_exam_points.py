import unittest
from institute import Institute
from main import ExamPoints, Student
from datetime import date

class TestAddExamPoints(unittest.TestCase):
    
    def test_1(self): # correct add(One object)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, 55.5, 30.0)
        inst = Institute()
        inst.add_examPoints(examPo)
        self.assertEqual(len(inst.exam_points), 1)
        
    def test_2(self): # correct add(Two objects)
        st1 = Student(172580, 'Петров Петр Петрович')
        st2 = Student(172584, "Иванов Иван Иванович")
        examPo1 = ExamPoints(st1, 55.5, 30.0)
        examPo2 = ExamPoints(st2, 40.0, 25.0)
        inst = Institute()
        inst.add_examPoints(examPo1)
        inst.add_examPoints(examPo2)
        self.assertEqual(len(inst.exam_points), 2)
        
    def test_3(self): # incorrect add(Existing object)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, 55.5, 30.0)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
            inst.add_examPoints(examPo)
        self.assertEqual("Exam point already exist", str(context.exception))
        self.assertEqual(len(inst.exam_points), 1)
        
    def test_4(self): # incorrect add(Wrong type)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(1)
        self.assertEqual("Wrong type", str(context.exception))
        self.assertEqual(len(inst.exam_points), 0)
        
    def test_5(self): # incorrect add(Wrong student type)
        examPo = ExamPoints(1, 55.5, 30.0)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
        self.assertEqual("Wrong student type", str(context.exception))
        self.assertEqual(len(inst.exam_points), 0)
        
    def test_6(self): # incorrect add(Wrong in points)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, -10., 30.0)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
        self.assertEqual("Wrong in points", str(context.exception)) 
        self.assertEqual(len(inst.exam_points), 0)
        
    def test_7(self): # incorrect add(Wrong exam points)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, 55.5, -10.)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
        self.assertEqual("Wrong exam points", str(context.exception)) 
        self.assertEqual(len(inst.exam_points), 0)
        
    def test_8(self): # incorrect add(Wrong in points type)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, "55.5", -10.)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
        self.assertEqual("Wrong in points type", str(context.exception)) 
        self.assertEqual(len(inst.exam_points), 0)
    
    def test_9(self): # incorrect add(Wrong exam points type)
        st = Student(172580, 'Петров Петр Петрович')
        examPo = ExamPoints(st, 55.5, "10.0")
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_examPoints(examPo)
        self.assertEqual("Wrong exam points type", str(context.exception)) 
        self.assertEqual(len(inst.exam_points), 0)
    
class TestGetExamPoints(unittest.TestCase):
    
    def test_1(self):
        pass