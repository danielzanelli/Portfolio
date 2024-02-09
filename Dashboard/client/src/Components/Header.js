import React from "react";
import logo from "../logo.png";
import { useLocation } from "react-router-dom";
import "../index.css";

function NavLink({ currentLocation, path, label }) {
  const isActive = currentLocation === path;
  const color = isActive ? "text-black" : "text-gray-500";
  const border = isActive ? "border-b-2 border-black" : "";

  return (
    <a
      className={`font-sans ${color} lg:text-2xl md:text-xl sm:text-base ${border} hover:text-black font-semibold text-center`}
      href={path}
    >
      {label}
    </a>
  );
}

function Header() {
  const isLoggedIn = JSON.parse(localStorage.getItem("Auth"));
  const location = useLocation().pathname;

  const links = isLoggedIn
    ? [
        { path: "/", label: "Home" },
        { path: "/logout", label: "Log Out" },
      ]
    : [
        { path: "/", label: "Home" },
        { path: "/login", label: "Log In" },
      ];

  return (
    <div className="flex bg-white shadow space-y-2">
      <img className="h-12 w-12 mr-10" src={logo} alt="icon" />
      <nav className="flex justify-between w-screen px-20">
        {links.map((link) => (
          <NavLink
            key={link.path}
            currentLocation={location}
            path={link.path}
            label={link.label}
          />
        ))}
      </nav>
    </div>
  );
}

export default Header;
