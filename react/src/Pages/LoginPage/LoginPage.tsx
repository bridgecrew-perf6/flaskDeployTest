import WalletConnectProvider from "@walletconnect/web3-provider";
import { connectWalletWithModal } from "../../Web3Communication/Web3Init";
import {
  MDBCardImage,
  MDBModal,
  MDBModalBody,
  MDBModalContent,
  MDBModalDialog,
  MDBModalFooter,
  MDBModalHeader,
  MDBModalTitle,
} from "mdb-react-ui-kit";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PagePaths } from "../../ReactConstants";

export function LoginPage() {
  const navigate = useNavigate();
  const [showModal, setShowModal] = useState<boolean>(true);
  return <></>;
}
