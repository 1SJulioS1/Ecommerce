import React from 'react'
import './ProductCardStyles.css'
const ProductCard = (props) => {
  return (
    <div className='product-card'>
      <h1>this is a productcard</h1>
      <h2>prodct name : {props.name}</h2>
      <h2>product description : {props.description}</h2>
      
    </div>
  )
}

export default ProductCard
