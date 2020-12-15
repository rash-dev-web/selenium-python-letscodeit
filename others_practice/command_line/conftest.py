import pytest


@pytest.fixture()
def set_up():
    print('one time setup')
    yield
    print('one time teardown')


@pytest.fixture(scope='module')
def one_time_set_up():
    print('running one time setup')
    yield
    print('running one time teardown')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='type of operating system')

def browser(request):
    return request.config.getOption('--browser')
