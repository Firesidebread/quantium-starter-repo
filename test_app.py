import pytest
from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    header = dash_duo.find_element("#header")
    assert header is not None

def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    visualization = dash_duo.find_element("#visualization")
    assert visualization is not None

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None