async def test_proxy_get_nested_url(cli):
    nested_part = "/nested/more_nested"

    with patch("src.app.get_path") as mock:
        # assert mock.return_value == nested_part
        pass
