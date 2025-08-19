import argparse, json, time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    if args.debug:
        print("[scanzaclip-core] Debug mode ON")
    # Placeholder scan logic
    print("Scanning clips... (stub)")
    time.sleep(0.5)
    print("Done.")

if __name__ == "__main__":
    main()
