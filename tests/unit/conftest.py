import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_periodic_exporting_metric_reader():
    """Globally mock PeriodicExportingMetricReader to prevent real network calls."""
    with patch(
        "google.cloud.spanner_v1.client.PeriodicExportingMetricReader"
    ) as mock_client_reader, patch(
        "opentelemetry.sdk.metrics.export.PeriodicExportingMetricReader"
    ):
        yield mock_client_reader
