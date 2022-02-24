from brownie import SimpleStorage, accounts, config


def readContract():
    simple_storage = SimpleStorage[-1]  # most recent deployment
    stored_value = simple_storage.retrive()
    print(stored_value)


def main():
    readContract()
