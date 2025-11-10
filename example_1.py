from config_compare.compare import config_compare

def main():
    print(config_compare(current="configs/current.conf", candidate="configs/candidate.conf", indent=4))

if __name__ == "__main__":
    main()