from locust import HttpUser, task, constant

class WebsiteUser(HttpUser):
    wait_time = constant(0)

    @task
    def load_pages(self):
        self.client.get("/")
        self.client.get("/")
