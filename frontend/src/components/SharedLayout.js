import { Outlet } from "react-router-dom";
import BottomNavBar from "./BottomNavBar";
import React from "react";
import CategoriesNavBar from "./CategoriesNavBar";
import { useState } from "react";

const SharedLayout = () => {
  const [activeSideNav, setActiveSideNav] = useState(false);
  const toggleSideNav = () => {
    setActiveSideNav(!activeSideNav);
  };
  return (
    <>
      <BottomNavBar switchSideNav={toggleSideNav}></BottomNavBar>

      {activeSideNav ? <CategoriesNavBar switchSideNav={toggleSideNav} /> : ""}
      <Outlet></Outlet>
    </>
  );
};

export default SharedLayout;
