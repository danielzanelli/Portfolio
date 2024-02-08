import React from "react";
import logo from "../logo.png";
import { NavLink, useLocation } from "react-router-dom";
import "../index.css";

function Header() {
  var isLoggedIn = function () {
    return JSON.parse(localStorage.getItem("Auth"));
  };

  var location = useLocation().pathname;

  if (isLoggedIn()) {
    return (
      <div class="flex  bg-white shadow space-y-2 ">
        <img class="h-12 w-12 mr-10" src={logo} alt="icon" />
        <nav class="flex justify-between w-screen px-20">
          {location === "/" ? (
            <a
              class=" font-sans text-black lg:text-2xl md:text-xl sm:text-baseborder-b-2 border-b-2 border-black hover:text-black font-semibold  text-center "
              href="/"
            >
              Home
            </a>
          ) : (
            <a
              class=" font-sans  text-gray-500 lg:text-2xl md:text-xl sm:text-base hover:text-black font-semibold  text-center "
              href="/data"
            >
              Home
            </a>
          )}
          {location === "/logout" ? (
            <a
              class=" font-sans text-black lg:text-2xl md:text-xl sm:text-baseborder-b-2 border-b-2 border-black hover:text-black font-semibold  text-center "
              href="/logout"
            >
              Log Out
            </a>
          ) : (
            <a
              class=" font-sans  text-gray-500 lg:text-2xl md:text-xl sm:text-base hover:text-black font-semibold  text-center "
              href="/logout"
            >
              Log Out
            </a>
          )}
        </nav>
      </div>
    );
  } else {
    return (
      <div class="flex  bg-white shadow space-y-2 ">
        <img class="h-12 w-12 mr-10" src={logo} alt="icon" />
        <nav class="flex justify-between w-screen px-20">
          {location === "/" ? (
            <a
              class=" font-sans text-black lg:text-2xl md:text-xl sm:text-baseborder-b-2 border-b-2 border-black hover:text-black font-semibold  text-center "
              href="/"
            >
              Home
            </a>
          ) : (
            <a
              class="font-sans  text-gray-500 lg:text-2xl md:text-xl sm:text-base hover:text-black font-semibold  text-center"
              href="/"
            >
              Home
            </a>
          )}
          {location === "/login" ? (
            <a
              class=" font-sans text-black lg:text-2xl md:text-xl sm:text-baseborder-b-2 border-b-2 border-black hover:text-black font-semibold  text-center "
              href="/login"
            >
              Log In
            </a>
          ) : (
            <a
              class="font-sans  text-gray-500 lg:text-2xl md:text-xl sm:text-base hover:text-black font-semibold  text-center"
              href="/login"
            >
              Log In
            </a>
          )}
        </nav>
      </div>
    );
  }
}

export default Header;
