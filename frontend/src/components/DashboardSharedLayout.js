import DashBoardSideNavBar from "./DashBoardSideNavBar";
import { Outlet } from "react-router-dom";

const DashboardSharedLayout = () => {
  return (
    <div className=" bg-slate-100">
      <div className="w-full h-10 bg-sky-900">
        <h1 className="text-white text-left ml-3  align-baseline">
          Torresuelto Admin Panel
        </h1>
      </div>
      <div className="flex">
        <DashBoardSideNavBar />
        {/* {add graph} */}
        <h1>Add main graph</h1>
        <Outlet></Outlet>
      </div>
    </div>
  );
};

export default DashboardSharedLayout;
