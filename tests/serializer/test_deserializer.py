# Imports
import pytest
from src.serializer import Deserializer, JSONDeserializer

# End Immports

@pytest.fixture
def deserializer():
    return Deserializer()

def check_implementaions(deserializer):
    assert isinstance(deserializer, JSONDeserializer)