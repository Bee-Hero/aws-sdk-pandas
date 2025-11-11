import beehero_awswrangler as wr


def test_metadata():
    assert wr.__version__ == "3.14.0"
    assert wr.__title__ == "beehero_awswrangler"
    assert wr.__description__ == "Pandas on AWS."
    assert wr.__license__ == "Apache License 2.0"
