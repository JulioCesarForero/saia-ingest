import pytest
import os

@pytest.fixture(scope="session")
def configuration():
    conf = {
        "saia": {
            "base_url": os.environ.get('BASE_URL'),
            "api_token": os.environ.get('API_TOKEN'),
            "profile": os.environ.get('ASSISTANT_NAME')
        }
    }
    print("Configuration:")
    print(f"BASE_URL: {conf['saia']['base_url']}")
    print(f"API_TOKEN: {conf['saia']['api_token']}")
    print(f"ASSISTANT_NAME: {conf['saia']['profile']}")
    return conf
