import pytest
import selenium


@pytest.fixture
def test_browser():

    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
