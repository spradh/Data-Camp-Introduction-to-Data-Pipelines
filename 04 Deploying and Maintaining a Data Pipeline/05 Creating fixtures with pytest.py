# Import pytest
import pytest

# Create a pytest fixture
@pytest.fixture()
def raw_tax_data():
	raw_data = extract("raw_tax_data.csv")
    
    # Return the raw DataFrame
	return raw_data
