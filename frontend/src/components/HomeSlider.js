import React from "react";
import { useState, useEffect } from "react";
import { BsChevronCompactLeft, BsChevronCompactRight } from "react-icons/bs";
import { RxDotFilled } from "react-icons/rx";
const HomeSlider = () => {
  const slides = [
    {
      url: "https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2620&q=80",
    },
    {
      url: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80",
    },
    {
      url: "https://images.unsplash.com/photo-1661961112951-f2bfd1f253ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2672&q=80",
    },

    {
      url: "https://images.unsplash.com/photo-1512756290469-ec264b7fbf87?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2253&q=80",
    },
    {
      url: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2671&q=80",
    },
  ];

  const [currentIndex, setCurrentIndex] = useState(0);

  const prevSlide = () => {
    const isFirstSlide = currentIndex === 0;
    const newIndex = isFirstSlide ? slides.length - 1 : currentIndex - 1;
    setCurrentIndex(newIndex);
  };

  const nextSlide = () => {
    const isLastSlide = currentIndex === slides.length - 1;
    const newIndex = isLastSlide ? 0 : currentIndex + 1;
    setCurrentIndex(newIndex);
  };

  const goToSlide = (slideIndex) => {
    setCurrentIndex(slideIndex);
  };
  //   useEffect(() => {

  //     const autoSlide = () => {
  //         return nextSlide()
  //       };

  //       setInterval( ()=>autoSlide , 100000)
  //   }, [])

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevImage) => (prevImage + 1) % slides.length);
    }, 5000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return (
    <div className="max-w-[1400px] h-[500px] mx-auto p-2 sm:py-20 group">
      <div
        style={{ backgroundImage: `url(${slides[currentIndex].url})` }}
        className="w-full h-full rounded-2xl bg-center bg-cover duration-500"
      >
        {/* Left Arrow */}
        <div className="flex lg:px-10 md:px-8 sm:px-6 w-fit float-left h-full rounded-xl py-6 group-hover:text-white text-transparent opacity-0 group-hover:opacity-100 transition-all text-2xl text-white cursor-pointer group-hover:backdrop-blur-sm ">
          <BsChevronCompactLeft
            className="my-auto"
            onClick={prevSlide}
            size={30}
          />
        </div>

        {/* Right Arrow */}
        <div className="flex lg:px-10 md:px-8 sm:px-6 w-fit float-right h-full rounded-xl py-6 group-hover:text-white text-transparent opacity-0 group-hover:opacity-100 transition-all text-2xl text-white cursor-pointer group-hover:backdrop-blur-sm ">
          <BsChevronCompactRight
            className=" my-auto"
            onClick={nextSlide}
            size={30}
          />
        </div>
      </div>

      <div className="flex top-4 hover:bg-gray-300 rounded-md m-auto w-fit transition-all h-fit justify-center px-0 mt-2">
        {slides.map((slide, slideIndex) => (
          <div
            key={slideIndex}
            onClick={() => goToSlide(slideIndex)}
            className="text-2xl   transition-all p-1 hover:rounded-full  cursor-pointer"
          >
            <RxDotFilled className="text-red-800 hover:text-white transition-all " />
          </div>
        ))}
      </div>
    </div>
  );
};

export default HomeSlider;
