import argparse

def test_permissions():
    print("[permission-control] Permissions OK (stub)")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        raise SystemExit(test_permissions())
