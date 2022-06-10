import { web3 } from "./Web3Init";

export async function getCurrAccount() {
  let accounts = await web3.eth.getAccounts();
  let currAccount = accounts[0];

  console.log("getCurrAccount() Returned: ", accounts[0]);
  console.log("All accounts: ", accounts);
  return currAccount;
}

export async function createContract(abi, address) {
  let contract = await new web3.eth.Contract(abi, address);
  console.log("creactContract() returning: ", contract);
  console.log("default account: ", contract.defaultAccount);

  return contract;
}
