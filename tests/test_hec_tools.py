#!/usr/bin/env python

"""Tests for `hec_tools` package."""

import pytest
import mock
import builtins

from click.testing import CliRunner

from hec_tools import hec_tools
from hec_tools import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'hec_tools.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


from hec_tools import hec_tools

def test_hec_tools():
    """Test hec_tools."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    # assert hms is instance of hec_tools.HMS
    assert isinstance(hms, hec_tools.HMS)

    with pytest.raises(FileNotFoundError):
        hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T2")

def test_get_hms_prjName():
    """Test get_hms_info."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    assert hms.prjName == "WestForkCalcasieu"

def test_get_run_names():
    """Test get_run_names."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    assert hms.run_name == "Run: 0.5_May_2020"

def test_get_run_names_prompt():
    """Test get_run_names."""

    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T")
    
    # add user input to test
    run_name = "Run: 0.5_May_2020"

    assert hms.run_name == run_name

def test_get_hms_loc():
    """Test get_hms_info."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    assert hms.loc == r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T"

def test_get_bat_loc():
    """Test get_bat_loc."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    assert hms.get_bat_loc() == r'hec_tools\HMScompute.bat'

def test_count_files():
    """Test count_files."""
    hms = hec_tools.HMS(r"C:\Users\christianl\repos\Sensitivity-Calibration\08_Calibration\TrialTester\HMS_T", prompt=False, run="Run: 0.5_May_2020")

    assert hms.count_files("*.run") == 1






