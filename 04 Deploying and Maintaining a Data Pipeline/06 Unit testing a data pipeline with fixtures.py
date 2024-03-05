# Define a pytest fixture
@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("raw_tax_data.csv")
    
    # Transform the raw_data, store in clean_data DataFrame, and return the variable
    clean_data = transform(raw_data)
    return clean_data

#2
# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert clean_tax_data["tax_rate"].max() <= 1 and clean_tax_data["tax_rate"].min() >= 0
