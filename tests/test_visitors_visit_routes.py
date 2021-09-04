from ward import test, expect
from fixtures import test_client


@test("must contains text")
def _(client=test_client):
    res = client.get("/")

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_in("Hello, World!", res.get_data(as_text=True), None)


@test("must contains text")
def _(client=test_client):
    res = client.get("/contact")

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_in("Contact page", res.get_data(as_text=True), None)


@test("must contains form")
def _(client=test_client):
    res = client.get("/new")

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_in("form", res.get_data(as_text=True), None)
    expect.assert_in("Send", res.get_data(as_text=True), None)


@test("must redirect to index")
def _(client=test_client):
    res = client.post("/create", follow_redirects=True)

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_equal(res.request.path, "/", None)
    expect.assert_in("Hello, World!", res.get_data(as_text=True), None)
