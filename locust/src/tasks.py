from locust import HttpUser, task, between

class LoadTesting(HttpUser):

    wait_time = between(1, 3)

    @task(1)
    def user_request(self):
        self.client.get("/")