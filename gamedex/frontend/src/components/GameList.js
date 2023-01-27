import React, { Component } from "react";
import { Table } from "reactstrap";
import NewGameModal from "./NewGameModal";


class GameList extends Component {
  render() {
    const games = this.props.games;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>APP Type</th>
            <th>URL</th>
            <th>Genres</th>
            <th>Developers</th>
            <th>Publishers</th>
            <th>Systems</th>
            <th>Published At</th>
            <th>Last Record</th>
          </tr>
        </thead>
        <tbody>
          {!games || games.length <= 0 ? (
            <tr>
              <td colSpan="9" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            games.map((game) => (
              <tr key={game.pk}>
                <td>{game.app_type}</td>
                <td>{game.link}</td>
                <td>{game.genres}</td>
                <td>{game.developers}</td>
                <td>{game.publishers}</td>
                <td>{game.systems}</td>
                <td>{game.published_at}</td>
                <td>{game.last_record}</td>
                <td align="center">
                  <NewGameModal
                    create={false}
                    game={game}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default GameList;
