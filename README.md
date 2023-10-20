# take-home-test-solution
A solution project to https://github.com/dfeinberg-rbi/take-home-test

## Intalling
Run command to install all necessary packages using [requirements.txt](requirements.txt) file
```
pip install -r requirements.txt
```

## Running API
Run the API locally by using `uvicorn`
```
uvicorn src.main.app:app --reload --port 3000
```

## Testing API
Run all tests using `pytest`
```
pytest
```