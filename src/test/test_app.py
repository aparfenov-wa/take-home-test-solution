from fastapi.testclient import TestClient

from src.main.app import app

client = TestClient(app)


def test_read_all_values():
    res = client.get("/survey_data")
    assert res.status_code == 200

def test_read_selected_columns():
    cols = ["timestamp", "company_name"]
    res = client.get(f"/survey_data?fields={','.join(cols)}")
    
    assert res.status_code == 200
    assert list(res.json()[0].keys()) == cols

def test_read_sorted():
    res = client.get("/survey_data?fields=salary_base_2018&sort=salary_base_2018")

    assert res.status_code == 200

    values = [list(item.values())[0] for item in res.json()]
    values = [v for v in values if v != 'nan']
    assert values == sorted(values)

