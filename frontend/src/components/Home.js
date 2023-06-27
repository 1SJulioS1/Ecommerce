import React from 'react'
// import { useState, useEffect } from 'react'
import ProductCard from './ProductCard'
import { Link } from 'react-router-dom'



const Home = () => {

  const products = [
    {
        id:12798327,
        name:'Samsung Cover',
        description:'black cover whith round corners',
        price:'10',
        image:'../mockImages/copiroyal-soluciones-grafing-detalleria-fundas-celulares.jpg'
    },
    {
        id:900238091,
        name:'iPhone Cover',
        description:'red cover whith square corners',
        price:'15',
        image:'../mockImages/depositphotos_54137009-stock-photo-mobile-phone-case.jpg'
    }
]

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
    <div>
      <h1>This is the home page</h1>
      <h2>List of products</h2>
      {products.map((each)=>
      <Link key={each.id} to={`/products/:${each.id}`}>
        <ProductCard key={each.id} name={each.name} description={each.description} image={each.image}></ProductCard>
      </Link>)
      } 
      


    </div>
  )
}

export default Home
