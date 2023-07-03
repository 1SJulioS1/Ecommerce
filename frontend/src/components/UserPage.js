import React from "react";
import { Link } from "react-router-dom";

const UserPage = () => {
  return (
    <div className=" flex flex-col my-[20vh] h-fit p-7 bg-slate-600 sm:w-fit rounded-lg m-auto ">
      <Link
        className=" bg-black text-white rounded-lg mb-10 p-3"
        to="/register"
      >
        Register
      </Link>
      <p className=" text-neutral-300"> Already have an account? </p>
      <Link className=" bg-black text-white rounded-lg p-3" to="/login">
        Login
      </Link>
    </div>
  );
};

export default UserPage;
