import React, { useEffect, useState } from "react";
import Header from "./Header.js";
import Lottie from "react-lottie";

function Public() {
  const [animationData, setAnimationData] = useState(null);

  useEffect(() => {
    fetch(
      "https://lottie.host/0f0cda83-78e9-4d5f-a1d1-746e6351f6e1/uSUtH3aJlQ.json"
    )
      .then((response) => response.json())
      .then((data) => setAnimationData(data))
      .catch((error) => console.log(error));
  }, []);

  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };

  return (
    <div className="flex flex-col overflow-auto h-screen bg-gray-100">
      <Header></Header>
      <div className="flex flex-col items-center my-20">
        <div className="align-middle flex flex-col max-w-lg p-8  text-center ">
          <h1 className="text-3xl font-bold p-8">Landing page</h1>
          <h1 className="text-md font-semibold text-gray-500 p-8">
            This is a demo of an IoT dashboard that allows to visualize data
            from the users devices.
          </h1>

          {animationData && (
            <div style={{ position: "relative" }}>
              <Lottie
                options={defaultOptions}
                height={300}
                width={300}
                isPaused={false}
                isStopped={false}
              />
              <div
                style={{
                  position: "absolute",
                  top: 0,
                  left: 0,
                  right: 0,
                  bottom: 0,
                }}
              />
            </div>
          )}

          <h1 className="text-md font-semibold text-gray-500 p-8">
            In order to access the dashboard, please log in.
          </h1>
        </div>
      </div>
    </div>
  );
}

export default Public;
