import subprocess

def test_func(user_codes_dir, test_files_dir, test_id):
    command = f'gcc "{user_codes_dir}/calculator.c" "{test_files_dir}/test-{test_id}/0-test_calculator.c" -o "{test_files_dir}/test-{test_id}/test" && "{test_files_dir}/test-{test_id}/test"'
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )
    exit_code = result.returncode
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    expected_stdout = ""
    expected_stderr = ""

    if exit_code == 0:
        result = {
            "id": test_id,
            "status": "pass",
            "message": "Test passed"
        }
        return result
    else:
        fail_reason = f"""
        [GOT]
        {stdout}
        {len(stdout)} chars long
        [stderr]:
        {stderr}
        {len(stderr)} chars long
        [EXPECTED]
        {expected_stdout}
        {len(expected_stdout)} chars long
        [stderr]:
        {expected_stderr}
        {len(expected_stderr)} chars long
        """
        result = {
            "id": test_id,
            "status": "fail",
            "message": fail_reason,
        }
        return result