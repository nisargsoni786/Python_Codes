import time
# from locust import HttpUser, task, between

# class QuickstartUser(HttpUser):
#     wait_time = between(1, 2.5)

#     @task
#     def hello_world(self):
#         # self.client.get("/a")
#         # self.client.get("/b")
#         # self.client.get("/c")
#         time.sleep(1)
#         self.client.get("/")
#         # self.client.get("/a")

#     @task
#     def hello_worldd(self):
#         # self.client.get("/a")
#         # self.client.get("/b")
#         # self.client.get("/c")
#         time.sleep(1)
#         self.client.get("/a")
#         # self.client.get("/a")
    
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    host='http://127.0.0.1:5000'
    wait_time = between(5.0, 9.0)

    @task
    def index(l):
        l.client.get("/")
        l.client.get('/a')

