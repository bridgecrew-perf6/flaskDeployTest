import React, { Dispatch, SetStateAction, useEffect, useState } from "react";
import {
  MDBBtn,
  MDBModal,
  MDBModalDialog,
  MDBModalContent,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter,
  MDBCardImage,
  MDBCardText,
} from "mdb-react-ui-kit";

import "../../../CSS/AppDetailsModal.css";
import "../../../CSS/appImage.css";
import AppData from "../../AppsPage/AppData";
import UpdateAppForm from "./UpdateAppForm";
import { toast } from "react-toastify";

interface UpdateAppModalProps {
  appToUpdate: AppData;
  showModal: boolean;
  setShowModal: Dispatch<SetStateAction<boolean>>;
  toggleShowModal: any;
  isLoading: boolean;
  setIsLoading: Dispatch<SetStateAction<boolean>>;
  setIsUploading: Dispatch<SetStateAction<boolean>>;
  isUploading: boolean;
}

export default function UpdateAppModal({
  appToUpdate,
  showModal,
  setShowModal,
  toggleShowModal,
  isLoading,
  setIsLoading,
  setIsUploading,
  isUploading,
}: UpdateAppModalProps) {
  const [imgUrl, setImgUrl] = useState<string>();

  useEffect(() => {
    setImgUrl(appToUpdate?.img_url);
    console.log(`App to update was set to ${appToUpdate.name}`);
  }, [appToUpdate]);

  function sleep(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  return (
    <>
      <MDBModal
        show={showModal}
        setShow={setShowModal}
        tabIndex={-1}
        staticBackdrop={isLoading}
      >
        <MDBModalDialog centered size={"lg"}>
          <MDBModalContent>
            <MDBModalHeader>
              <MDBModalTitle>{`Update ${appToUpdate.name}`}</MDBModalTitle>
            </MDBModalHeader>
            <MDBModalBody>
              <UpdateAppForm
                setIsLoading={setIsLoading}
                currAppData={appToUpdate}
                isLoading={isLoading}
                isUploading={isUploading}
                setIsUploading={setIsUploading}
                setShowModal={setShowModal}
              ></UpdateAppForm>
            </MDBModalBody>
          </MDBModalContent>
        </MDBModalDialog>
      </MDBModal>
    </>
  );
}
/*              <MDBBtn>Purchase</MDBBtn>
 */

/*

 <MDBCardImage
                src={imgUrl ? imgUrl : app.img_url ? app.img_url : no_image_alt}
                position="top"
                alt="..."
                className="app-image"
              />
              <h4 id="description-paragraph-title">Description:</h4>
              <p id="description-paragraph" className="card-text">
                {app.description}
              </p>
 */
