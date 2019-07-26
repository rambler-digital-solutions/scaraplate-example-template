from pkg_resources import get_distribution


def test_metadata():
    metadata_name = "{{ cookiecutter.metadata_name }}"
    pkg = get_distribution(metadata_name)
    assert pkg.version
    assert pkg.project_name == metadata_name


def test_package_import():
    import {{ cookiecutter.python_package }}

    assert {{ cookiecutter.python_package }}
