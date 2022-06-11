import json
from web3Init import web3
from web3._utils.events import get_event_data

dappstore_address = "0x6a5B11650FA8187B35d9a792632e88C2f0Ad1A37"
dappstore_abi = json.loads(""" [{
        "inputs": [{
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
        "inputs": [{
            "internalType": "uint256",
            "name": "num_apps",
            "type": "uint256"
        }],
        "name": "createXApps",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{
            "internalType": "uint256",
            "name": "app_id",
            "type": "uint256"
        }],
        "name": "purchaseApp",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [{
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
        "inputs": [{
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
        "outputs": [{
            "components": [{
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
                    "name": "num_ratings",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "rating",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "rating_modulu",
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
                }
            ],
            "internalType": "struct AppInfoLibrary.AppInfo[]",
            "name": "",
            "type": "tuple[]"
        }],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAppCount",
        "outputs": [{
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
        }],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{
            "internalType": "string",
            "name": "",
            "type": "string"
        }],
        "stateMutability": "view",
        "type": "function"
    },
    {
    "anonymous": false,
    "inputs": [
        {
            "indexed": true,
            "internalType": "string",
            "name": "app_name",
            "type": "string"
        },
        {
            "indexed": true,
            "internalType": "uint256",
            "name": "app_id",
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
            "internalType": "address",
            "name": "sender",
            "type": "address"
        }
    ],
    "name": "AppCreated",
    "type": "event"
},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "app_creator",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "app_contract",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "dapp_store",
				"type": "address"
			}
		],
		"name": "UserPurchased",
		"type": "event"
	}
]""")


dappstore_contract = web3.eth.contract(address=dappstore_address, abi=dappstore_abi)

# app_created_filter =  dappstore_contract.events.AppCreated.createFilter(fromBlock='latest')
app_created_filter =  dappstore_contract.events.AppCreated.createFilter(fromBlock= 0)
user_purchased_filter =  dappstore_contract.events.UserPurchased.createFilter(fromBlock= 0)

# event_template = dappstore_contract.events.AppCreated

# print("ABI: ", event_template._get_event_abi())

# events = web3.eth.get_logs({'fromBlock':0, 'address':"0x6a5B11650FA8187B35d9a792632e88C2f0Ad1A37"})
# print(events)
# print("EVENTS LEN: ", len(events))

# def handle_event(event, event_template):
#     print("Handlign Event: {}\n\n".format(event))
    
#     try:
#         result = get_event_data(event_template.web3.codec, event_template._get_event_abi(), event)
#         return True, result
#     except Exception as e:
#         print("Error: {}".format(e))
#         return False, None

# for event in events: 
#     suc, res = handle_event(event=event, event_template=event_template)   
#     if suc:
#         print("Event found", res)

"""
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "string",
				"name": "app_name",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "app_id",
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
				"internalType": "address",
				"name": "sender",
				"type": "address"
			}
		],
		"name": "AppCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "oldOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnerSet",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "string",
				"name": "content_type",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "string",
				"name": "previous_content",
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
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "sender",
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
				"name": "app_creator",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address payable",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "app_contract",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "dapp_store",
				"type": "address"
			}
		],
		"name": "UserPurchased",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "changeOwner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]


"""