import React, { Component } from "react";
import "./App.css";
import Header from "./Components/Header.js";

class Public extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoginOpen: true,
      isRegisterOpen: false,
      user: {},
    };
  }
  render() {
    return (
      <div class="flex flex-col overflow-auto h-screen bg-gray-100">
        <Header></Header>
        <div class="flex flex-col items-center my-20">
          <div class="align-middle flex flex-col max-w-lg p-8  text-center ">
            <h1 class="text-3xl font-bold p-8">Landing page</h1>
            <h1 class="text-md font-semibold text-gray-500 p-8">
              This is a demo of an IoT dashboard that allows to visualize data
              from the users devices.
            </h1>
            <h1 class="text-md font-semibold text-gray-500 p-8">
              In order to access the dashboard, please log in.
            </h1>
          </div>
        </div>
      </div>
    );
  }
}

export default Public;
