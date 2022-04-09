# from tests.routes.test_main import client

# def test_login():
#     response = client.post(
#         url="/api/auth/login",
#         data={"grant_type": "password", "username": "123", "password": "123"},
#     )
#     assert response.status_code == 200
#     print(response.json())
#     assert response.json() == {"access_token": str, "token_type": "bearer"}
#     pass


# def test_registration():
#     response = client.get("/api/auth/register")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello Application!"}
#     pass
