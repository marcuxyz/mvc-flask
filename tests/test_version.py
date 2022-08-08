from mvc_flask.__version__ import __version__
from ward import test, expect


@test("check version")
def _():
    expect.assert_equal(__version__, "2.4.0", None)
