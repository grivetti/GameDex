import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import GameList from "./GameList";
import NewGameModal from "./NewGameModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    games: [],
  };

  componentDidMount() {
    this.resetState();
  }

  getGames = () => {
    axios.get(API_URL).then((res) => this.setState({ games: res.data }));
  };

  resetState = () => {
    this.getGames();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <GameList games={this.state.games} resetState={this.resetState} />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewGameModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
