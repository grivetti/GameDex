import React, { Component, Fragment } from "react";
import {Modal, ModalHeader, ModalBody } from "reactstrap";

class NewGameModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    return (
      <Fragment>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader></ModalHeader>
          <ModalBody>
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewGameModal;