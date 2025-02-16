import pytest
from click.testing import CliRunner

from newshomepages import wayback


@pytest.mark.vcr()
def test_wayback_cli(tmp_path):
    """Test a single wayback archive request."""
    runner = CliRunner()
    result = runner.invoke(wayback.cli, ["reuters", "-o", tmp_path, "--verbose"])
    assert result.exit_code == 0
