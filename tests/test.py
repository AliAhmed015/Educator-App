import pytest
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app

COURSE_ID = None


@pytest.mark.asyncio
async def test_course_flow():
    """End-to-end test for Courses module with REAL JWT TOKEN."""

    transport = ASGITransport(app=app)

    async with LifespanManager(app):
        async with AsyncClient(transport=transport, base_url="http://test") as client:

            # ---------------------------------------------------------
            # 0. LOGIN AND GET REAL TOKEN
            # ---------------------------------------------------------
            login_payload = {
                "name": "Ali",
                "email": "ali@example.com",
                "password": "321",
                "role": "admin"
            }



            res = await client.post("/admin_login", json=login_payload)
            assert res.status_code == 200

            token = res.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            # print("Response body:", res.json())

            # ---------------------------------------------------------
            # 1. CREATE COURSE
            # ---------------------------------------------------------
            create_payload = {
                "title": "Advanced Python Test",
                "description": "Deep dive into Python",
                "teacher": "John Doe",
                "price": 199.99
            }

            res = await client.post("/course", json=create_payload, headers=headers)

            # Already exists → 409, otherwise success → 201
            assert res.status_code in (201, 307, 409)

            global COURSE_ID
            COURSE_ID = create_payload["title"]
            print("COURSE_ID:", COURSE_ID)

            # ---------------------------------------------------------
            # 2. LIST COURSES
            # ---------------------------------------------------------
            res = await client.get("/courses", headers=headers)
            print("Status Code for List Courses:", res.status_code)
            assert res.status_code == 200

            courses = res.json()
            assert isinstance(courses, list)
            print("Courses:", courses)

            # ---------------------------------------------------------
            # 3. GET SPECIFIC COURSE
            # ---------------------------------------------------------
            res = await client.get(f"/course/{COURSE_ID}", headers=headers)
            assert res.status_code == 200
            assert res.json()["title"] == "Advanced Python Test"

            # ---------------------------------------------------------
            # 4. UPDATE COURSE
            # ---------------------------------------------------------
            update_payload = {
                "title": "Advanced Python Test - Updated",
                "description": "Updated course description",
                "teacher": "Jane Doe",
                "price": 249.99
            }

            res = await client.put(f"/course/{COURSE_ID}", json=update_payload, headers=headers)
            assert res.status_code == 200

            # ---------------------------------------------------------
            # 5. DELETE COURSE
            # ---------------------------------------------------------
            res = await client.delete(f"/course/{COURSE_ID}", headers=headers)
            assert res.status_code == 200
            print("Delete Response:", res.json())
            assert res.json()["message"] == f"Course with title '{COURSE_ID}' deleted successfully"

            # ---------------------------------------------------------
            # 6. NEGATIVE – DELETE AGAIN
            # ---------------------------------------------------------
            res = await client.delete(f"/course/{COURSE_ID}", headers=headers)
            assert res.status_code == 404

            # ---------------------------------------------------------
            # 7. NEGATIVE – GET NON‑EXISTING COURSE
            # ---------------------------------------------------------
            res = await client.get(f"/course/670000000000000000000000", headers=headers)
            assert res.status_code == 404

            # ---------------------------------------------------------
            # 8. NEGATIVE – CREATE WITH NO DATA
            # ---------------------------------------------------------
            res = await client.post("/course/", json={}, headers=headers)
            assert res.status_code in (307, 422)

            # ---------------------------------------------------------
            # 9. LIST AGAIN
            # ---------------------------------------------------------
            res = await client.get("/courses", headers=headers)
            assert res.status_code == 200
