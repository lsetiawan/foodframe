def test_package_import():
    import foodframe
    
    assert foodframe.__version__ is not None
