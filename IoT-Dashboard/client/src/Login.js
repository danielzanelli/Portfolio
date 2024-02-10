import React, { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";
import Header from "./Header.js";

//const api = "https://demo.automatype.com/api/";
const api = "http://localhost:5000/api/";

function Login() {
  const [formState, setFormState] = useState({ name: "", password: "" });

  const handleChange = (e) => {
    setFormState({
      ...formState,
      [e.target.name]: e.target.value,
    });
  };

  useEffect(() => {
    const authCheck = () => {
      axios
        .get(api + "users/authchecker", {
          headers: {
            "Content-type": "application/json",
          },
          withCredentials: true,
        })
        .then((res) => {
          localStorage.setItem("Auth", true);
          window.location.href = "/";
        })
        .catch((error) => {
          localStorage.setItem("Auth", false);
        });
    };

    authCheck();
    localStorage.setItem("API", api);
  }, []);

  const onFormSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const formDataObj = Object.fromEntries(formData.entries());

    axios
      .post(api + "users/login", formDataObj, {
        headers: {
          "Content-type": "application/json",
        },
        withCredentials: true,
      })
      .then((res) => {
        localStorage.setItem("tel_data", JSON.stringify([]));
        localStorage.setItem("const_data", JSON.stringify([]));
        localStorage.setItem("events", JSON.stringify([]));

        var sync_values = {
          tel_data: "0",
          const_data: "0",
          events: "0",
        };

        localStorage.setItem("Sync", JSON.stringify(sync_values));
        localStorage.setItem("Auth", true);

        localStorage.setItem("graph1", JSON.stringify([12, 19, 3, 5, 2]));
        localStorage.setItem("graph2", JSON.stringify([11, 18, 13]));
        localStorage.setItem(
          "graph3_1",
          JSON.stringify([
            {
              x: new Date(new Date().getTime() - 2000),
              y: 10 * Math.random(),
            },
            { x: new Date(), y: 10 * Math.random() },
          ])
        );
        localStorage.setItem(
          "graph3_2",
          JSON.stringify([
            {
              x: new Date(new Date().getTime() - 2000),
              y: 20 * Math.random(),
            },
            { x: new Date(), y: 20 * Math.random() },
          ])
        );
        localStorage.setItem(
          "graph4_1",
          JSON.stringify([
            {
              x: new Date(new Date().getTime() - 2000),
              y: 15 * Math.random(),
            },
            { x: new Date(), y: 15 * Math.random() },
          ])
        );
        localStorage.setItem(
          "graph4_2",
          JSON.stringify([
            {
              x: new Date(new Date().getTime() - 2000),
              y: -10 * Math.random(),
            },
            { x: new Date(), y: -10 * Math.random() },
          ])
        );

        window.location.href = "/";
      })
      .catch((error) => {
        console.log(error);
        localStorage.setItem("Auth", false);
      });
  };

  return (
    <div className="items-center h-screen bg-gray-100">
      <Header></Header>
      <div className="flex flex-col items-center my-20">
        <div className="align-middle flex flex-col max-w-lg p-8 shadow-lg rounded-xl text-center bg-white">
          <h1 className="text-3xl font-bold ">Log In</h1>
          <h3 className="text-md font-semibold text-gray-500">
            Log in to your account
          </h3>
          <form className="mt-5" onSubmit={onFormSubmit}>
            <div>
              <input
                className="p-1 my-3 rounded-lg bg-gray-100 shadow-md focus:outline-none focus:border-2 border-cyan-500"
                placeholder="Username"
                name="name"
                type="text"
                onChange={handleChange}
              />
            </div>

            <div>
              <input
                className="p-1 my-3 rounded-lg bg-gray-100 shadow-md focus:outline-none focus:border-2 border-cyan-500"
                placeholder="Password"
                name="password"
                type="password"
                onChange={handleChange}
              />
            </div>

            <input
              className="p-2 pr-5 pl-5 text-white font-semibold rounded-xl bg-gray-800 hover:bg-black m-4"
              value="LOG IN"
              type="submit"
            />
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
