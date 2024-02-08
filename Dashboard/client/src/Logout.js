import React, { Component } from "react";
import "./App.css";
import axios from "axios";
import localForage from "localforage";

class Logout extends Component {
  render() {
    axios
      .delete(localStorage.getItem("API") + "users/logout", {
        headers: {
          "Content-type": "application/json",
        },
        crossDomain: true,
        withCredentials: true,
      })
      .then((res) => {
        //console.log(`statusCode: ${res.status}`);
        //console.log(res);
        localStorage.clear();
        localForage.clear();
        window.location.href = "/login";
      })
      .catch((error) => {
        console.log(error);
        localStorage.clear();
        localForage.clear();
        window.location.href = "/login";
      });

    return <h1>Bye</h1>;
  }
}

export default Logout;
