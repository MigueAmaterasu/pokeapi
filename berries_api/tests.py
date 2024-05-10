from unittest.mock import patch

import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
@patch("berries_api.views.requests.get")
def test_all_berry_stats(mock_get):
    mock_response = {
        "results": [
            {"name": "berry1", "url": "url1"},
            {"name": "berry2", "url": "url2"},
            {"name": "berry3", "url": "url3"},
        ]
    }

    mock_berry_data = {"growth_time": 10}

    mock_get.side_effect = [mock_response, mock_berry_data, mock_berry_data, mock_berry_data]

    client = Client()
    response = client.get(reverse("all_berry_stats"))

    assert response.status_code == 200
    assert response.json() == {
        "berries_names": ["berry1", "berry2", "berry3"],
        "min_growth_time": 10,
        "median_growth_time": 10,
        "max_growth_time": 10,
        "variance_growth_time": 0,
        "mean_growth_time": 10,
        "frequency_growth_time": {10: 3},
    }
