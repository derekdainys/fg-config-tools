import argparse
from config_compare.compare import config_compare

def main():
    parser = argparse.ArgumentParser(description="A program that will show a diff between two fortinet configurations")
    parser.add_argument("--current", help="name of the file for running config")
    parser.add_argument("--candidate", help="name of the file for the candidate config")

    args = parser.parse_args()
    diff_config = config_compare(current=args.current, candidate=args.candidate, indent=4)
    revert_config = config_compare(current=args.candidate, candidate=args.current, indent=4)
    print(f"Current -> Candidate")
    print("*" * 50)
    print(diff_config)

    print(f"Revert: Candidate -> Current")
    print("*" * 50)
    print(revert_config)


if __name__ == "__main__":
    main()