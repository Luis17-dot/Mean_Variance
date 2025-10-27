import pytest
import pandas as pd
import demographic_data_analyzer


def test_calculate_demographic_data():
    result = demographic_data_analyzer.calculate_demographic_data(
        print_data=False)

    # Check if all required keys are present in the result
    required_keys = [
        'race_count', 'average_age_men', 'percentage_bachelors',
        'higher_education_rich', 'lower_education_rich', 'min_work_hours',
        'rich_percentage', 'highest_earning_country',
        'highest_earning_country_percentage', 'top_IN_occupation'
    ]
    for key in required_keys:
        assert key in result, f"Missing key: {key}"

    # Verify data types and some basic validations
    assert isinstance(result['race_count'],
                      pd.Series), "race_count should be a pandas Series"
    assert isinstance(result['average_age_men'],
                      float), "average_age_men should be a float"
    assert isinstance(result['percentage_bachelors'],
                      float), "percentage_bachelors should be a float"
    assert 0 <= result['percentage_bachelors'] <= 100, "percentage_bachelors should be between 0 and 100"
    assert isinstance(result['min_work_hours'],
                      int), "min_work_hours should be an integer"
    assert result['min_work_hours'] >= 0, "min_work_hours should be non-negative"


if __name__ == "__main__":
    pytest.main([__file__])
