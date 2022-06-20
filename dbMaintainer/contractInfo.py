import json
from web3Init import web3
from web3._utils.events import get_event_data

dappstore_address = "0xE6277ECb7E1097224D063Ecfaa011d16784c7BDC"
dappstore_abi = json.loads("""
                          [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_magnetLink",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_imgUrl",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_category",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_fileSha256",
				"type": "string"
			}
		],
		"name": "createNewApp",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "start",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "len",
				"type": "uint256"
			}
		],
		"name": "getAppBatch",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "imgUrl",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "company",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numRatings",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingInt",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingModulu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "userRating",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fileSha256",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "owned",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "magnetLink",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "publishTime",
						"type": "uint256"
					}
				],
				"internalType": "struct AppInfoLibrary.AppInfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAppCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_app_id",
				"type": "uint256"
			}
		],
		"name": "getAppRating",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getPublishedAppsInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "imgUrl",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "company",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numRatings",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingInt",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingModulu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "userRating",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fileSha256",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "owned",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "magnetLink",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "publishTime",
						"type": "uint256"
					}
				],
				"internalType": "struct AppInfoLibrary.AppInfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getPurchasedAppsInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "imgUrl",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "company",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numRatings",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingInt",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingModulu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "userRating",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fileSha256",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "owned",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "magnetLink",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "publishTime",
						"type": "uint256"
					}
				],
				"internalType": "struct AppInfoLibrary.AppInfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getRatedAppsInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "imgUrl",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "company",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numRatings",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingInt",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingModulu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "userRating",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fileSha256",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "owned",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "magnetLink",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "publishTime",
						"type": "uint256"
					}
				],
				"internalType": "struct AppInfoLibrary.AppInfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_app_id",
				"type": "uint256"
			}
		],
		"name": "getUserRatingForApp",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "app_id",
				"type": "uint256"
			}
		],
		"name": "purchaseApp",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_app_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "new_rating",
				"type": "uint256"
			}
		],
		"name": "rateApp",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "app_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_magnetLink",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_imgUrl",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_fileSha256",
				"type": "string"
			}
		],
		"name": "updateApp",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
 {
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "creator",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "company",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "category",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "description",
				"type": "string"
			}
		],
		"name": "AppCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "imgUrl",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "company",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numRatings",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingInt",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ratingModulu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "userRating",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "fileSha256",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "owned",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "magnetLink",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "publishTime",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct AppInfoLibrary.AppInfo",
				"name": "",
				"type": "tuple"
			}
		],
		"name": "AppInfo",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "app_id",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "rating_int",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "rating_modulu",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "num_ratings",
				"type": "uint256"
			}
		],
		"name": "AppRated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "app_id",
				"type": "uint256"
			}
		],
		"name": "UpdatedApp",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "app_id",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "string",
				"name": "content_type",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "string",
				"name": "new_content",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "previous_content",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			}
		],
		"name": "UpdatedContent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "user_address",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "user_contract",
				"type": "address"
			}
		],
		"name": "UserCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "app_id",
				"type": "address"
			}
		],
		"name": "UserPurchasedApp",
		"type": "event"
	}
]
""")


dappstore_contract = web3.eth.contract(address=dappstore_address, abi=dappstore_abi)

app_created_filter =  dappstore_contract.events.AppCreated.createFilter(fromBlock= 0)
user_purchased_filter =  dappstore_contract.events.UserPurchasedApp.createFilter(fromBlock= 0)
app_rated_filter =  dappstore_contract.events.AppRated.createFilter(fromBlock= 0)
# app_updated_filter = dappstore_contract.events.UpdatedContent.createFilter(fromBlock= 0)
app_updated_filter = dappstore_contract.events.UpdatedApp.createFilter(fromBlock= 0)

