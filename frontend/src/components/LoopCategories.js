import React from "react";

const LoopCategories = () => {
  const categories = [
    "Smartphones",
    "Laptops",
    "Tablets",
    "Headphones",
    "Speakers",
    "Televisions",
    "Cameras",
    "Smartwatches",
    "Gaming Consoles",
    "Printers",
    "Routers",
    "External Hard Drives",
    "Mouses",
    "Keyboards",
    "Monitors",
    "Chargers",
    "Batteries",
    "USB Cables",
    "Bluetooth Earbuds",
    "Microphones",
  ];

  return (
    <div className=" bg-sky-900 text-white py-1 w-full overflow-hidden">
      <ul className="flex w-full justify-around scrollLetters flex-wrap">
        {categories.map((each, i) => (
          <li
            className=" h-fit transition-all rounded-md p-1 hover:scale-105 hover:text-black hover:bg-white"
            key={i}
          >
            <a href="#">{each}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LoopCategories;
