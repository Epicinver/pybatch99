import subprocess

def run_batch(command: str, *, new_window=False, capture_output=False):
    """
    Execute a Windows batch command.

    Args:
        command (str): The batch command to run.
        new_window (bool): If True, runs in a new CMD window.
        capture_output (bool): If True, returns stdout/stderr from the command.

    Returns:
        subprocess.CompletedProcess or None
    """
    if new_window:
        subprocess.Popen(
            ["cmd", "/k", command],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return None
    else:
        return subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=capture_output
        )
