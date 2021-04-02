import pytest
import yaml


@pytest.mark.parametrize('param', yaml.load(open('./yaml_data.yaml', 'r', encoding='utf-8')))
def test_yaml():
    print()
