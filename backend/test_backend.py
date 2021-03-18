import requests


def test_testcase_post():
    r = requests.post(
        "http://127.0.0.1:5000/testcase",
        json={
            "name":"testcase4",
            "steps":["step1","step2"]
        }
    )
    assert r.status_code ==200

    r = requests.post(
        "http://127.0.0.1:5000/testcase",
        json={
            "name":"testcase3",
            "steps":["step1","step2"]
        }
    )
    assert r.status_code ==200


    r = requests.delete(
        "http://127.0.0.1:5000/testcase",
        json={
            "name":"testcase3"
        }
    )
    assert r.status_code ==200