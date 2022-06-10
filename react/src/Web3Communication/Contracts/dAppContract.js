import { createContract } from "../Web3Utils";

export const DAPPSTORE_CONTRACT_ADDRESS =
  "0x1024f69C9F88639A72A8123A3a03ebdeD2E0A803"; //Version 5 Rinkeby, getApps requires sender
//"0xded7fF8aA48c2Cf503d90B9b15f784cBf201f299"; //Version 4 Rinkeby, can purchase apps
//"0xf57E8de4645c45a0c93DC59a5A2D765BBEC8c53E"; //Version 3 Rinkeby, with get purchased & uploaded & update apps
//"0x9fb632ad470c88cc858206b24b2b1a1d46b8c001"; //Version 2 Rinkeby
// "0x343f80e459c60b6e1EEae3E469a95213DD3c36C0"; //Version 1 Rinkeby
//"0xa1879B8f434c0BE3ABb662A269F72496C7047d9E"; //GANACHE

//Version 2
export const DAPPSTORE_ABI = [
  {
    inputs: [
      {
        internalType: "uint256",
        name: "id",
        type: "uint256",
      },
    ],
    name: "purchase",
    outputs: [],
    stateMutability: "payable",
    type: "function",
  },
  {
    inputs: [],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "id",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "description",
        type: "string",
      },
      {
        internalType: "string",
        name: "fileSha256",
        type: "string",
      },
      {
        internalType: "string",
        name: "imgUrl",
        type: "string",
      },
      {
        internalType: "string",
        name: "magnetLink",
        type: "string",
      },
      {
        internalType: "uint256",
        name: "price",
        type: "uint256",
      },
    ],
    name: "update",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "string",
        name: "_name",
        type: "string",
      },
      {
        internalType: "string",
        name: "_description",
        type: "string",
      },
      {
        internalType: "string",
        name: "_fileSha256",
        type: "string",
      },
      {
        internalType: "string",
        name: "_imgUrl",
        type: "string",
      },
      {
        internalType: "string",
        name: "_magnetLink",
        type: "string",
      },
      {
        internalType: "string",
        name: "_company",
        type: "string",
      },
      {
        internalType: "uint256",
        name: "_price",
        type: "uint256",
      },
    ],
    name: "upload",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "apps",
    outputs: [
      {
        internalType: "uint256",
        name: "id",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "name",
        type: "string",
      },
      {
        internalType: "string",
        name: "description",
        type: "string",
      },
      {
        internalType: "address payable",
        name: "creator",
        type: "address",
      },
      {
        internalType: "string",
        name: "magnetLink",
        type: "string",
      },
      {
        internalType: "string",
        name: "imgUrl",
        type: "string",
      },
      {
        internalType: "string",
        name: "company",
        type: "string",
      },
      {
        internalType: "int256",
        name: "rating",
        type: "int256",
      },
      {
        internalType: "uint256",
        name: "price",
        type: "uint256",
      },
      {
        internalType: "uint256",
        name: "RatingsNum",
        type: "uint256",
      },
      {
        internalType: "bool",
        name: "owned",
        type: "bool",
      },
      {
        internalType: "int256",
        name: "myRating",
        type: "int256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "from",
        type: "uint256",
      },
      {
        internalType: "uint256",
        name: "to",
        type: "uint256",
      },
      {
        internalType: "address",
        name: "fetcher",
        type: "address",
      },
    ],
    name: "getApps",
    outputs: [
      {
        components: [
          {
            internalType: "uint256",
            name: "id",
            type: "uint256",
          },
          {
            internalType: "string",
            name: "name",
            type: "string",
          },
          {
            internalType: "string",
            name: "description",
            type: "string",
          },
          {
            internalType: "address payable",
            name: "creator",
            type: "address",
          },
          {
            internalType: "string[]",
            name: "fileSha256",
            type: "string[]",
          },
          {
            internalType: "string",
            name: "magnetLink",
            type: "string",
          },
          {
            internalType: "string",
            name: "imgUrl",
            type: "string",
          },
          {
            internalType: "string",
            name: "company",
            type: "string",
          },
          {
            internalType: "int256",
            name: "rating",
            type: "int256",
          },
          {
            internalType: "uint256",
            name: "price",
            type: "uint256",
          },
          {
            internalType: "uint256",
            name: "RatingsNum",
            type: "uint256",
          },
          {
            internalType: "bool",
            name: "owned",
            type: "bool",
          },
          {
            internalType: "int256",
            name: "myRating",
            type: "int256",
          },
        ],
        internalType: "struct dAppStore.App[]",
        name: "result",
        type: "tuple[]",
      },
      {
        internalType: "uint256",
        name: "totalNumOfApps",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "publisher",
        type: "address",
      },
    ],
    name: "getPublishedApps",
    outputs: [
      {
        components: [
          {
            internalType: "uint256",
            name: "id",
            type: "uint256",
          },
          {
            internalType: "string",
            name: "name",
            type: "string",
          },
          {
            internalType: "string",
            name: "description",
            type: "string",
          },
          {
            internalType: "address payable",
            name: "creator",
            type: "address",
          },
          {
            internalType: "string[]",
            name: "fileSha256",
            type: "string[]",
          },
          {
            internalType: "string",
            name: "magnetLink",
            type: "string",
          },
          {
            internalType: "string",
            name: "imgUrl",
            type: "string",
          },
          {
            internalType: "string",
            name: "company",
            type: "string",
          },
          {
            internalType: "int256",
            name: "rating",
            type: "int256",
          },
          {
            internalType: "uint256",
            name: "price",
            type: "uint256",
          },
          {
            internalType: "uint256",
            name: "RatingsNum",
            type: "uint256",
          },
          {
            internalType: "bool",
            name: "owned",
            type: "bool",
          },
          {
            internalType: "int256",
            name: "myRating",
            type: "int256",
          },
        ],
        internalType: "struct dAppStore.App[]",
        name: "publishedApps",
        type: "tuple[]",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "owner",
        type: "address",
      },
    ],
    name: "getPurchasedApps",
    outputs: [
      {
        components: [
          {
            internalType: "uint256",
            name: "id",
            type: "uint256",
          },
          {
            internalType: "string",
            name: "name",
            type: "string",
          },
          {
            internalType: "string",
            name: "description",
            type: "string",
          },
          {
            internalType: "address payable",
            name: "creator",
            type: "address",
          },
          {
            internalType: "string[]",
            name: "fileSha256",
            type: "string[]",
          },
          {
            internalType: "string",
            name: "magnetLink",
            type: "string",
          },
          {
            internalType: "string",
            name: "imgUrl",
            type: "string",
          },
          {
            internalType: "string",
            name: "company",
            type: "string",
          },
          {
            internalType: "int256",
            name: "rating",
            type: "int256",
          },
          {
            internalType: "uint256",
            name: "price",
            type: "uint256",
          },
          {
            internalType: "uint256",
            name: "RatingsNum",
            type: "uint256",
          },
          {
            internalType: "bool",
            name: "owned",
            type: "bool",
          },
          {
            internalType: "int256",
            name: "myRating",
            type: "int256",
          },
        ],
        internalType: "struct dAppStore.App[]",
        name: "purchasedApps",
        type: "tuple[]",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "personalRatings",
    outputs: [
      {
        internalType: "int256",
        name: "",
        type: "int256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "publishedListMapping",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "purchasedListMapping",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "ratingOrderedApps",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
];
