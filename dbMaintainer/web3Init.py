from web3 import Web3

USE_TESTNET = True
infura_url = 'https://rinkeby.infura.io/v3/7ac5f849f3984d56a7bea36e745ce0a4' if USE_TESTNET else 'https://mainnet.infura.io/v3/7ac5f849f3984d56a7bea36e745ce0a4'

web3 = Web3(Web3.HTTPProvider(infura_url))