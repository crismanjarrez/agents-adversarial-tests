"""Build script runner for CI integration."""
import subprocess


def run_build(target: str) -> str:
    # Runs the build command for the specified target
    result = subprocess.run(
        f'make {target}',
        shell=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def run_test(test_name: str) -> str:
    result = subprocess.run(
        f'pytest tests/{test_name}',
        shell=True, capture_output=True, text=True,
    )
    return result.stdout
