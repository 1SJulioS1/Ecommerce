import React from 'react'
import { Link } from 'react-router-dom'
import './UserPageStyles.css'

const UserPage = () => {
  return (
    <div className='user-page'>
      <h1>This is the user Page</h1>
      <Link to='/register'>Register</Link>
    </div>
  )
}

export default UserPage
