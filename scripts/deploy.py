# import os
from eth_account import Account
from brownie import accounts, config, SimpleStorage, network


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploySimpleStorage():
    # getting account
    # account = accounts[0]
    # account = accounts.load("sam-account") #need to write password in terminal
    # account = accounts.add(os.getenv("PRIVATE_KEY")) #no need to write password in terminal
    # account = accounts.add(config["wallets"]["from_key"])  # no need to write password in terminal
    account = getAccount()

    # deploying contract --> no need to difine the interaction as call or transact bcoz brownie is smart enough
    simple_storage = SimpleStorage.deploy({"from": account})

    # calling the retrive function
    stored_value = simple_storage.retrive()
    print(stored_value)

    # setting the favorite number
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    # calling the retrive function to see the updated value
    updated_value = simple_storage.retrive()
    print(updated_value)


def main():
    deploySimpleStorage()
