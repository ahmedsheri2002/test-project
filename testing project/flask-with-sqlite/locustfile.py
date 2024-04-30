from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  # Add a random wait time between requests

    @task
    def index(self):
        self.client.get("/")  # Send a GET request to the home page

    @task
    def add_student(self):
        self.client.get("/addstudent")  # Send a GET request to the add student page

    @task
    def list_students(self):
        self.client.get("/list")  # Send a GET request to list students page

    @task
    def add_student_post(self):
        # Send a POST request to addrec endpoint with some dummy data
        self.client.post("/addrec", data={"name": "John Doe", "address": "123 Main St", "city": "Anytown", "pin": "12345"})

    # You can add more tasks to simulate various user interactions with your Flask application
