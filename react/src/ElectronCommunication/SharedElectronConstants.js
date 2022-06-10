const isElectron = require("is-electron");

const REACT_ADDRESS = "http://localhost:3000";
const IS_ON_ELECTRON = isElectron();
const IS_DEBUG = false;

module.exports = {
  REACT_ADDRESS,
  IS_DEBUG,
  IS_ON_ELECTRON,
};
