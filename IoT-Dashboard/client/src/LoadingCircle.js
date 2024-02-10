import React from "react";

function LoadingCircle() {
  return (
    <div class="align-middle m-8 flex flex-col max-w-lg p-8 shadow-lg rounded-xl text-center bg-white overflow-y-auto max-h-screen">
      <div
        style={{ "border-top-color": "transparent" }}
        class="w-16 h-16 border-4 border-gray-700 border-solid rounded-full animate-spin"
      />
    </div>
  );
}

export default LoadingCircle;
