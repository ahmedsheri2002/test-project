import unittest
from app import app

class FlaskIntegrationTest(unittest.TestCase):
    
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    # Test adding a new student and then listing all students to check if the new student is added
    def test_add_student_and_list_students(self):
        # Make a POST request to add a new student
        self.app.post('/addrec', data=dict(name='John Doe', address='123 Main St', city='Anytown', pin='12345'))
        # Make a GET request to list all students
        response = self.app.get('/list')
        # Check if the response contains the name of the added student
        self.assertIn(b'John Doe', response.data)

    # Test accessing the home page
    def test_home_page_access(self):
        response = self.app.get('/')
        # Check if the home page returns the expected status code
        self.assertEqual(response.status_code, 200)
        # Check if the home page contains the expected content
        self.assertIn(b'Home Page', response.data)

    # Test accessing the add student page
    def test_add_student_page_access(self):
        response = self.app.get('/addstudent')
        # Check if the add student page returns the expected status code
        self.assertEqual(response.status_code, 200)
        # Check if the add student page contains the expected content
        self.assertIn(b'Add New Student', response.data)

    # Test accessing the list students page
    def test_list_students_page_access(self):
        response = self.app.get('/list')
        # Check if the list students page returns the expected status code
        self.assertEqual(response.status_code, 200)
        # Check if the list students page contains the expected content
        self.assertIn(b'List of Students', response.data)

if __name__ == '__main__':
    unittest.main()

