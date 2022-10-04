import random

from locust import TaskSet, HttpUser, task, between


class GetByBookId(TaskSet):
    @task(1)
    def get_books(self):
        print("--> Performing an API Call to get by Book Id")
        headers = {
            "accept": "text/plain; v=1.0"
        }
        inputnum = random.randint(1, 100)
        with self.client.get(
                url="/api/v1/Authors/authors/books/"+str(inputnum),
                headers=headers,
                catch_response=True,
                name="Get_Book_ById"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [GetByBookId]
    wait_time = between(0.00001, 0.0004)
