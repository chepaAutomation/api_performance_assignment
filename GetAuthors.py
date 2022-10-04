from locust import TaskSet, HttpUser, task, between


class GetAuthorsAPICall(TaskSet):
    @task(1)
    def get_authors(self):
        print("--> Performing an API Call to get author details")
        headers = {
            "accept": "text/plain; v=1.0"
        }
        with self.client.get(
                url="/api/v1/Authors",
                headers=headers,
                catch_response=True,
                name="Get_Authors_Detail"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [GetAuthorsAPICall]
    wait_time = between(0.00001, 0.0004)
