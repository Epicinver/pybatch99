from pybatch99 import run_batch

def test_echo():
    result = run_batch("echo Hello from batch, inside of python!", capture_output=True)
    assert "Hello from batch, inside of python!" in result.stdout

def test_new_window():
    # This should open a new CMD window and run the command.
    # It won't return anything to the current script.
    run_batch("echo Hello in python using new window is false && pause", new_window=False)

if __name__ == "__main__":
    print("[*] Testing...")
    test_new_window()
    print("[✓] Tested.")
