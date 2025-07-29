from pybatch99 import run_batch

def test_echo():
    result = run_batch("echo Hello from batch!", capture_output=True)
    assert "Hello from batch!" in result.stdout

def test_new_window():
    # This should open a new CMD window and run the command.
    # It won't return anything to the current script.
    run_batch("echo Hello in new window && pause", new_window=True)

if __name__ == "__main__":
    print("[*] Running captured output test...")
    test_echo()
    print("[✓] Captured output test passed.")

    print("[*] Launching new window test (close it manually)...")
    test_new_window()
    print("[✓] New window test launched.")
