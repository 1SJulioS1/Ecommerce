import { Outlet } from "react-router-dom";
import BottomNavBar from "./BottomNavBar";
import React from 'react'

const SharedLayout = () => {
  return (
    <div>
      <BottomNavBar></BottomNavBar>
      <Outlet></Outlet>
    </div>
  )
}

export default SharedLayout
