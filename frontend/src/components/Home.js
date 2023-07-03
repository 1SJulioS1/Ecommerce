import React from "react";
// import { useState, useEffect } from 'react'
import ProductCard from "./ProductCard";
import { Link } from "react-router-dom";
import HomeSlider from "./HomeSlider";
import HomePagination from "./HomePagination";
import Footer from "./Footer";
import LoopCategories from "./LoopCategories";

const Home = () => {
  const products = [
    {
      id: 12798327,
      name: "Samsung Cover",
      description: "black cover whith round corners",
      price: "10",
      image:
        "../mockImages/copiroyal-soluciones-grafing-detalleria-fundas-celulares.jpg",
    },
    {
      id: 900238091,
      name: "iPhone Cover",
      description: "red cover whith square corners",
      price: "15",
      image:
        "../mockImages/depositphotos_54137009-stock-photo-mobile-phone-case.jpg",
    },
    {
      id: 900238091,
      name: "iPhone Cover",
      description: "red cover whith square corners",
      price: "15",
      image:
        "../mockImages/depositphotos_54137009-stock-photo-mobile-phone-case.jpg",
    },
    {
      id: 900238091,
      name: "iPhone Cover",
      description: "red cover whith square corners",
      price: "15",
      image:
        "../mockImages/depositphotos_54137009-stock-photo-mobile-phone-case.jpg",
    },
    {
      id: 900238091,
      name: "iPhone Cover",
      description: "red cover whith square corners",
      price: "15",
      image:
        "../mockImages/depositphotos_54137009-stock-photo-mobile-phone-case.jpg",
    },
  ];

  //   const [posts,setPosts] = useState();
  //   useEffect(() => {
  //     fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
  //        .then((response) => response.json())
  //        .then((data) => {
  //           console.log(data);
  //           setPosts(data);
  //        })
  //        .catch((err) => {
  //           console.log(err.message);
  //        });
  //  }, []);

  return (
    <div className="w-auto mx-auto">
      <LoopCategories></LoopCategories>
      <HomeSlider />
      <h1>This is the home page</h1>
      <h2 className="sr-only">Products</h2>
      <div className="bg-white">
        <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
          <div className="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
            {products.map((each, index) => (
              <Link
                key={index}
                to={`/products/:${each.id}`}
                className="group hover:shadow-2xl transition-all"
              >
                <ProductCard
                  key={each.id}
                  name={each.name}
                  description={each.description}
                  image={each.image}
                ></ProductCard>
              </Link>
            ))}
          </div>
        </div>
      </div>
      <HomePagination></HomePagination>
      <Footer></Footer>
    </div>
  );
};

export default Home;
