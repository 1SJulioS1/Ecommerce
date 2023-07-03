import { useEffect, useState } from "react";

const CategoriesNavBar = ({ switchSideNav }) => {
  const [categories, setCategories] = useState({});
  useEffect(() => {
    try {
      fetch("http://127.0.0.1:8000/api/category/")
        .then((response) => response.json())
        .then((data) => setCategories(data));
    } catch (error) {
      console.log(error);
    }
  }, []);
  //   const categories = ["Accesories", "Smartphones", "Subscriptions"];

  return (
    <div className=" fixed inset-0 bg-black bg-opacity-25 backdrop-blur-xs transition-all">
      <div className="h-full w-full flex ">
        <ul className="lg:w-[600px] sm:w-[300px] shadow-lg  glass">
          <h1 className="py-5 shadow-lg bg-slate-200">Shop by categories</h1>
          <li className=" bg-gray-50 text-left px-3 py-3">
            {categories.count}
          </li>

          {/* {categories.results.map((result, index) => (
            <li key={index}>{JSON.stringify(result)}</li>
          ))} */}
        </ul>
        <button onClick={switchSideNav} className=" h-full w-full"></button>
      </div>
    </div>
  );
};

export default CategoriesNavBar;
