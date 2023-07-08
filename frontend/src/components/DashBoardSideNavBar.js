import React from "react";
import { NavLink } from "react-router-dom";
import { FaUsers } from "react-icons/fa";
import { PiListChecks } from "react-icons/pi";
import {
  MdOutlineProductionQuantityLimits,
  MdOutlineInventory,
} from "react-icons/md";
import { GoGraph } from "react-icons/go";
import { RiDashboard3Fill } from "react-icons/ri";

const DashBoardSideNavBar = () => {
  const navlinkStyles = "flex items-center transition-all gap-2 p-2 ";

  return (
    <div className="flex flex-col text-left bg-gray-200 h-screen w-2/12">
      <NavLink className={navlinkStyles} to="/admin">
        <RiDashboard3Fill />
        Dashboard
      </NavLink>
      <NavLink className={navlinkStyles} to="/admin/users">
        <FaUsers />
        Users
      </NavLink>
      <NavLink className={navlinkStyles} to="/admin/orders">
        <PiListChecks />
        Orders
      </NavLink>
      <NavLink className={navlinkStyles} to="/admin/products">
        <MdOutlineProductionQuantityLimits />
        Products
      </NavLink>
      <NavLink className={navlinkStyles} to="/admin/graphs">
        <GoGraph />
        Graphs
      </NavLink>
      <NavLink className={navlinkStyles} to="/admin/inventory">
        <MdOutlineInventory />
        Inventory
      </NavLink>
    </div>
  );
};

export default DashBoardSideNavBar;
