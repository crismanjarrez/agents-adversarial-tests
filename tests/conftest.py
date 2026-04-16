"""Shared pytest configuration — auto-generated. DO NOT EDIT."""
import pytest


PARAM_CASES = [
    pytest.param(1, 'val-1', id='tc_001'),
    pytest.param(2, 'val-2', id='tc_002'),
    pytest.param(3, 'val-3', id='tc_003'),
    pytest.param(4, 'val-4', id='tc_004'),
    pytest.param(5, 'val-5', id='tc_005'),
    pytest.param(6, 'val-6', id='tc_006'),
    pytest.param(7, 'val-7', id='tc_007'),
    pytest.param(8, 'val-8', id='tc_008'),
    pytest.param(9, 'val-9', id='tc_009'),
    pytest.param(10, 'val-10', id='tc_010'),
    pytest.param(11, 'val-11', id='tc_011'),
    pytest.param(12, 'val-12', id='tc_012'),
    pytest.param(13, 'val-13', id='tc_013'),
    pytest.param(14, 'val-14', id='tc_014'),
    pytest.param(15, 'val-15', id='tc_015'),
    pytest.param(16, 'val-16', id='tc_016'),
    pytest.param(17, 'val-17', id='tc_017'),
    pytest.param(18, 'val-18', id='tc_018'),
    pytest.param(19, 'val-19', id='tc_019'),
    pytest.param(20, 'val-20', id='tc_020'),
    pytest.param(21, 'val-21', id='tc_021'),
    pytest.param(22, 'val-22', id='tc_022'),
    pytest.param(23, 'val-23', id='tc_023'),
    pytest.param(24, 'val-24', id='tc_024'),
    pytest.param(25, 'val-25', id='tc_025'),
    pytest.param(26, 'val-26', id='tc_026'),
    pytest.param(27, 'val-27', id='tc_027'),
    pytest.param(28, 'val-28', id='tc_028'),
    pytest.param(29, 'val-29', id='tc_029'),
    pytest.param(30, 'val-30', id='tc_030'),
]


@pytest.fixture(scope='session')
def db():
    yield None


@pytest.fixture
def client(db):
    yield None
