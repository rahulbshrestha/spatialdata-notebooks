from napari_spatialdata._interactive import Interactive
from run_notebook import execute_notebook, add_parameters_to_cell



def test_add_parameters_to_cell():

    cell_text = "Interactive(sdata=sdata, headless=True)"
    expected_text = "Interactive(sdata=sdata, headless=True, coordinate_system_name=global, _tested_notebook=test_notebook.ipynb, _test_target=cell5, _take_screenshot=True)"

    assert add_parameters_to_cell(cell_text, take_screenshot=True) == expected_text


def test_add_parameters_to_cell_no_interactive():

    cell_text = "print('Hello world')"
    expected_text = cell_text

    assert add_parameters_to_cell(cell_text, take_screenshot=True) == expected_text


def test_add_parameters_to_cell_take_screenshot_is_false():

    cell_text = "Interactive(sdata=sdata, headless=True)"
    expected_text = "Interactive(sdata=sdata, headless=True, coordinate_system_name=global, _tested_notebook=test_notebook.ipynb, _test_target=cell5, _take_screenshot=False)"


    assert add_parameters_to_cell(cell_text, take_screenshot=False) == expected_text



def test_add_parameters_to_cell_screenshot_overwrite():

    cell_text = "Interactive(sdata=sdata, headless=True, coordinate_system_name=global, _tested_notebook=test_notebook.ipynb, _test_target=cell5, _take_screenshot=False)"
    expected_text = "Interactive(sdata=sdata, headless=True, coordinate_system_name=global, _tested_notebook=test_notebook.ipynb, _test_target=cell5, _take_screenshot=True)"

    assert add_parameters_to_cell(cell_text, take_screenshot=True) == expected_text