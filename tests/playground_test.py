from __future__ import annotations

from lib_sandbox_001.playground import toy_001


def test_toy_001():
    with pytest.raises(NotImplementedError, match='The toy_001 function is not yet implemented.'):
        toy_001()
