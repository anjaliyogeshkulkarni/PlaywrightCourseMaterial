from playwright.sync_api import sync_playwright, APIResponse
import logging
import Demo1_FirstProgram

class APIUtils:

    # POST Request (local API)
    def postRequest(self, playwright):
        api_request_context = playwright.request.new_context(base_url="http://127.0.0.1:5000")
        response = api_request_context.post("/demo_post_endpoint", data={'name': 'Jane', 'age': 12},
                                            headers={'Content-Type': 'application/json'})
        # failure condition data object missing
        # response = api_request_context.post("/my_post_endpoint", headers={'Content-Type': 'application/json'})
        return response

    def getRequest(self, playwright) -> APIResponse:
        context = playwright.request.new_context(
            base_url="http://127.0.0.1:5000"
        )
        response = context.get("/demo_get_endpoint")
        # context.dispose()
        print("GET API Response output: ", response.json())
        return response

    def deleteRequest(self,playwright):
        baseURL = "http://127.0.0.1:5000"
        api_endpoint = "/demo_delete_endpoint"
        api_request_context = playwright.request.new_context(base_url=baseURL)
        response = api_request_context.delete(api_endpoint)
        return response

#
# def test_APIPOSTRequest():
#     logging.basicConfig(filename="api_test.log", level=logging.INFO,
#                         format="%(asctime)s - %(levelname)s - %(message)s", force=True)
#     api_utils = APIUtils()
#     try:
#         with sync_playwright() as p:
#             response = api_utils.postRequest(p)
#             logging.info(f"Response JSON: {response.json()}")
#             assert response.status == 200
#             print("\nResponse : ", response)
#             print("\nResponse in JSON format: ", response.json())
#             print("Message in Response in JSON format: ", response.json().get('chars_added'))
#
#     except Exception as e:
#         logging.error(f"Test failed: {e}")
#         print(f"Test failed: {e}")
#
# def test_APIGETRequest():
#     logging.basicConfig(filename="api_test.log", level=logging.INFO,
#                         format="%(asctime)s - %(levelname)s - %(message)s", force=True)
#     api_utils = APIUtils()
#     try:
#         with sync_playwright() as p:
#             response = api_utils.getRequest(p)
#             logging.info(f"Response JSON: {response.json()}")
#             assert response.status == 200
#             print("Test passed!")
#     except Exception as e:
#         logging.error(f"Test failed: {e}")
#         print(f"Test failed: {e}")
#
# def test_APIDELETERequest():
#     logging.basicConfig(filename="api_test.log", level=logging.INFO,
#                         format="%(asctime)s - %(levelname)s - %(message)s", force=True)
#     apiUtils = APIUtils()
#     try:
#         with sync_playwright() as p:
#             response = apiUtils.deleteRequest(p)
#             logging.info(f"Response JSON: {response.json()}")
#             assert response.status == 200
#             print("Test passed!")
#             print("Delete API Response output: ", response)
#             print(response.json())
#     except Exception as e:
#         logging.error(f"Test failed: {e}")
#         assert False, f"Test case failed: {e}"

if __name__ == "__main__":
    # test_APIPOSTRequest()
    # test_APIGETRequest()
    # test_APIDELETERequest()
    Demo1_FirstProgram.swagLabs_Page()
