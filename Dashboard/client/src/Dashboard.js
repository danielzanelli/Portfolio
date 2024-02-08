import React, { useState, useEffect } from "react";
import axios from "axios";
import localForage from "localforage";
import "./App.css";
import Header from "./Components/Header.js";
import Public from "./Public.js";
import LoadingCircle from "./Components/LoadingCircle.js";
import { Bar, Line } from "react-chartjs-2";
import Chart from "chart.js/auto";
import "chartjs-adapter-moment";

const dataLimit = 100;

function Dashboard() {
  const auth = () => {
    axios
      .get(localStorage.getItem("API") + "users/authchecker", {
        headers: {
          "Content-type": "application/json",
        },
        withCredentials: true,
      })
      .then((res) => {
        localStorage.setItem("Auth", true);
        setLoaded(true);
      })
      .catch((e) => {
        localStorage.setItem("Auth", false);
        setReload(true);
        //this.props.history.push("/logout")
      });
  };

  const randValue = () => {
    return Math.random() * 2 - 1;
  };

  const update = () => {
    var graph1 = JSON.parse(localStorage.getItem("graph1"));
    var graph2 = JSON.parse(localStorage.getItem("graph2"));
    var graph3_1 = JSON.parse(localStorage.getItem("graph3_1"));
    var graph3_2 = JSON.parse(localStorage.getItem("graph3_2"));
    var graph4_1 = JSON.parse(localStorage.getItem("graph4_1"));
    var graph4_2 = JSON.parse(localStorage.getItem("graph4_2"));

    if (graph3_1.length > dataLimit) {
      graph3_1 = graph3_1.slice(1, graph3_1.length);
    }
    if (graph3_2.length > dataLimit) {
      graph3_2 = graph3_2.slice(1, graph3_2.length);
    }
    if (graph4_1.length > dataLimit) {
      graph4_1 = graph4_1.slice(1, graph4_1.length);
    }
    if (graph4_2.length > dataLimit) {
      graph4_2 = graph4_2.slice(1, graph4_2.length);
    }

    localStorage.setItem(
      "graph1",
      JSON.stringify([
        graph1[0] + randValue(),
        graph1[1] + randValue(),
        graph1[2] + randValue(),
        graph1[3] + randValue(),
        graph1[4] + randValue(),
      ])
    );
    localStorage.setItem(
      "graph2",
      JSON.stringify([
        graph2[0] + randValue(),
        graph2[1] + randValue(),
        graph2[2] + randValue(),
      ])
    );
    localStorage.setItem(
      "graph3_1",
      JSON.stringify(
        graph3_1.concat({
          x: new Date(),
          y: graph3_1[graph3_1.length - 1].y + randValue(),
        })
      )
    );
    localStorage.setItem(
      "graph3_2",
      JSON.stringify(
        graph3_2.concat({
          x: new Date(),
          y: graph3_2[graph3_2.length - 1].y + randValue(),
        })
      )
    );
    localStorage.setItem(
      "graph4_1",
      JSON.stringify(
        graph4_1.concat({
          x: new Date(),
          y: graph4_1[graph4_1.length - 1].y + randValue(),
        })
      )
    );
    localStorage.setItem(
      "graph4_2",
      JSON.stringify(
        graph4_2.concat({
          x: new Date(),
          y: graph4_2[graph4_2.length - 1].y + randValue(),
        })
      )
    );

    setGraph1(JSON.parse(localStorage.getItem("graph1")));
    setGraph2(JSON.parse(localStorage.getItem("graph2")));
    setGraph3_1(JSON.parse(localStorage.getItem("graph3_1")));
    setGraph3_2(JSON.parse(localStorage.getItem("graph3_2")));
    setGraph4_1(JSON.parse(localStorage.getItem("graph4_1")));
    setGraph4_2(JSON.parse(localStorage.getItem("graph4_2")));
  };

  const [loaded, setLoaded] = useState(false);
  const [reload, setReload] = useState(false);
  const [count, setCount] = useState(0);

  const [graph1, setGraph1] = useState(
    JSON.parse(localStorage.getItem("graph1"))
  );
  const [graph2, setGraph2] = useState(
    JSON.parse(localStorage.getItem("graph2"))
  );
  const [graph3_1, setGraph3_1] = useState(
    JSON.parse(localStorage.getItem("graph3_1"))
  );
  const [graph3_2, setGraph3_2] = useState(
    JSON.parse(localStorage.getItem("graph3_2"))
  );
  const [graph4_1, setGraph4_1] = useState(
    JSON.parse(localStorage.getItem("graph4_1"))
  );
  const [graph4_2, setGraph4_2] = useState(
    JSON.parse(localStorage.getItem("graph4_2"))
  );

  if (localStorage.getItem("Auth") === "true") {
    auth();
  }

  useEffect(() => {
    const interval = setInterval(() => {
      if (localStorage.getItem("Auth") === "true") {
        auth();
        update();
      } else {
        return;
      }
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    setReload(false);
    setCount(count + 1);
  }, [reload]);

  if (localStorage.getItem("Auth") !== "true") {
    return <Public></Public>;
  } else {
    return (
      <div
        id="page-wrapper"
        class="flex flex-col overflow-auto h-screen bg-gray-100"
      >
        <Header></Header>
        {loaded ? (
          <div class="flex flex-col w-100 items-center ">
            <h1 class="text-3xl font-bold p-8">Dashboard</h1>
            <h3 class="text-md font-semibold text-gray-500">
              This is a demo dashboard, this data is fake.
            </h3>

            <div class="flex w-11/12 center flex-wrap justify-evenly items-center">
              <div
                key={0}
                class=" lg:w-2/5 md:w-11/12 sm:w-11/12 align-middle flex flex-col mx-2 my-4 p-1 shadow-lg rounded-xl text-center bg-white"
              >
                <div class="flex flex-row justify-between items-center">
                  <div class="w-9/10"></div>
                </div>
                <h3 class="text-lg font-semibold text-gray-500">Bar Graph 1</h3>
                <div class="flex flex-col items-center align-middle  shadow-lg rounded-xl text-center bg-white ">
                  <Bar
                    id={0}
                    data={{
                      labels: ["A", "B", "C", "D", "E"],
                      datasets: [
                        {
                          data: graph1,
                          backgroundColor: "rgba(0,0,0,1.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "black",
                        },
                      ],
                    }}
                    options={{
                      plugins: {
                        legend: {
                          display: false,
                        },
                      },
                    }}
                  />
                </div>
              </div>
              <div
                key={1}
                class=" lg:w-2/5 md:w-11/12 sm:w-11/12 align-middle flex flex-col mx-2 my-4 p-1 shadow-lg rounded-xl text-center bg-white"
              >
                <div class="flex flex-row justify-between items-center">
                  <div class="w-9/10"></div>
                </div>
                <h3 class="text-lg font-semibold text-gray-500">Bar Graph 2</h3>
                <div class="flex flex-col items-center align-middle  shadow-lg rounded-xl text-center bg-white ">
                  <Bar
                    id={1}
                    data={{
                      labels: ["F", "G", "H"],
                      datasets: [
                        {
                          data: graph2,
                          backgroundColor: "rgba(0,0,0,1.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "black",
                        },
                      ],
                    }}
                    options={{
                      plugins: {
                        legend: {
                          display: false,
                        },
                      },
                    }}
                  />
                </div>
              </div>
              <div
                key={2}
                class=" lg:w-2/5 md:w-11/12 sm:w-11/12 align-middle flex flex-col mx-2 my-4 p-1 shadow-lg rounded-xl text-center bg-white"
              >
                <div class="flex flex-row justify-between items-center">
                  <div class="w-9/10"></div>
                </div>
                <h3 class="text-lg font-semibold text-gray-500">
                  Line Graph 1
                </h3>
                <div class="flex flex-col items-center align-middle  shadow-lg rounded-xl text-center bg-white ">
                  <Line
                    id={0}
                    type="line"
                    data={{
                      labels: [],
                      datasets: [
                        {
                          data: graph3_1,
                          label: "A",
                          backgroundColor: "rgba(0,0,0,0.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "black",
                        },
                        {
                          data: graph3_2,
                          label: "B",
                          backgroundColor: "rgba(0,0,0,0.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "green",
                        },
                      ],
                    }}
                    options={{
                      scales: {
                        x: { type: "time", time: { tooltipFormat: "LTS" } },
                      },
                      animation: false,
                    }}
                  />
                </div>
              </div>
              <div
                key={3}
                class=" lg:w-2/5 md:w-11/12 sm:w-11/12 align-middle flex flex-col mx-2 my-4 p-1 shadow-lg rounded-xl text-center bg-white"
              >
                <div class="flex flex-row justify-between items-center">
                  <div class="w-9/10"></div>
                </div>
                <h3 class="text-lg font-semibold text-gray-500">
                  Line Graph 2
                </h3>
                <div class="flex flex-col items-center align-middle  shadow-lg rounded-xl text-center bg-white ">
                  <Line
                    id={0}
                    type="line"
                    data={{
                      labels: [],
                      datasets: [
                        {
                          data: graph4_1,
                          label: "A",
                          backgroundColor: "rgba(0,0,0,0.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "black",
                        },
                        {
                          data: graph4_2,
                          label: "B",
                          backgroundColor: "rgba(0,0,0,0.0)",
                          pointBorderWidth: 0,
                          pointHoverBorderWidth: 1,
                          borderColor: "green",
                        },
                      ],
                    }}
                    options={{
                      scales: {
                        x: { type: "time", time: { tooltipFormat: "LTS" } },
                      },
                      animation: false,
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div class="flex flex-col items-center">
            <LoadingCircle />
          </div>
        )}
      </div>
    );
  }
}

export default Dashboard;
