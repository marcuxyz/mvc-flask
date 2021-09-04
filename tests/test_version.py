from mvc_flask.__version__ import __version__
from ward import test, expect


@test("gets version")
def _():
    expect.assert_equal(__version__, "0.1.0", None)
