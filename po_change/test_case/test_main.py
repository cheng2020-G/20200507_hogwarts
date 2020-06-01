# coding=utf-8
import pytest
import yaml

from po_change.page.app import App


class TestMain:
    # @pytest.mark.skip
    def test_main(self):
        app = App()
        app.start().main().goto_search()

    @pytest.mark.skip
    def test_search(self):
        app = App()
        app.start().main().steps()
