import Web3 from "web3";
import Web3Modal from "web3modal";
import WalletConnectProvider from "@walletconnect/web3-provider";
import { connectWalletWithModal } from "./Web3Init";
import {
  helloWorldABI,
  HELLO_WORLD_ADDRESS,
} from "./Contracts/helloworldContract";
import { getCurrAccount, createContract } from "./Web3Utils";
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: "7ac5f849f3984d56a7bea36e745ce0a4",
    },
  },
};

export function Web3TestPage() {
  return (
    <>
      <button onClick={() => connectWalletWithModal()}>
        Connect to rinkeby
      </button>
      <button onClick={() => connectWalletWithModal("HTTP://127.0.0.1:7545")}>
        Connect to ganache
      </button>
      <button
        onClick={async () => {
          let contract = await createContract(
            helloWorldABI,
            HELLO_WORLD_ADDRESS
          );
          let res = contract.methods
            .message()
            .call()
            .then((res: any) => {
              console.log("HelloWorld Contract Value = ", res);
            })
            .catch((error: any) => {
              console.log("ERROR in getContractValue", error);
            });
        }}
      >
        Print HelloWorld Contract Value
      </button>
      <button
        onClick={async () => {
          let contract = await createContract(
            helloWorldABI,
            HELLO_WORLD_ADDRESS
          );

          let from = await getCurrAccount();
          console.log("from: ", from);
          contract.methods
            .setMessage("abra")
            .send({ from: from })
            .then((res: any) => {
              console.log("HelloWorld Contract Value was set.");
            })
            .catch((error: any) => {
              console.log("ERROR in setContract", error);
            });
        }}
      >
        Set Contract Value to "ABC"
      </button>
      <button
        onClick={() => {
          getCurrAccount();
        }}
      >
        Print Current Acocunt
      </button>
    </>
  );
}
