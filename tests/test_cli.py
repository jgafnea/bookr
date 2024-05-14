from unittest.mock import patch

import pytest

from src.console import run


def test_without_arguments():
    with pytest.raises(SystemExit) as e:
        with patch("sys.argv", [""]):
            run()

    assert e.type == SystemExit
    assert e.value.code == 2
