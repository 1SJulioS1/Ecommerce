import React from 'react'
import { useParams } from 'react-router-dom'

const SingleProduct = () => {
    const {productId} = useParams()
  return (
    <div>
        this is a single product with this id:{productId}
        
    </div>
  )
}

export default SingleProduct
