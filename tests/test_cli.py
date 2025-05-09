from click.testing import CliRunner
from modern_python_template.cli import main

def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version 0.1.0" in result.output

def test_process_command():
    runner = CliRunner()
    result = runner.invoke(main, ["process", "input.txt"])
    assert result.exit_code == 0
    assert "Processing input.txt..." in result.output

def test_help_output():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert "SYNOPSIS" in result.output
    assert "DESCRIPTION" in result.output
    assert "Commands" in result.output
    assert "config" in result.output
    assert "process" in result.output