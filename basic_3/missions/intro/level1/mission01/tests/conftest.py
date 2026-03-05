"""mission01 conftest — submission_dir fixture 제공"""
import os

import pytest

_MISSION_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_SUBMISSION = os.path.join(_MISSION_DIR, "sample_submission")


@pytest.fixture(scope="session")
def submission_dir(request):
    cli_value = request.config.getoption("--submission-dir")
    resolved = os.path.abspath(cli_value) if cli_value else _DEFAULT_SUBMISSION
    assert os.path.isdir(resolved), f"제출물 디렉토리 없음: {resolved}"
    return resolved


@pytest.fixture(scope="session")
def data_path():
    """data/data.json 절대 경로 제공"""
    path = os.path.join(_MISSION_DIR, "data", "data.json")
    assert os.path.isfile(path), f"data.json 파일 없음: {path}"
    return path
