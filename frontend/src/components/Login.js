import React, { useContext } from 'react'
import { useState,useRef,useEffect } from 'react'
import { Link } from 'react-router-dom'
import './LoginStyles.css'
import  AuthContext  from '../context/AuthProvider'
import axios from '../api/axios'
const LOGIN_URL = '/api/login/'

const Login = () => {
    const {setAuth} = useContext(AuthContext);
    const userRef = useRef();
    const errRef = useRef();

    const [user,setUser] = useState('');
    const [pwd, setPwd] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess]= useState(false)

    useEffect(()=>{
        userRef.current.focus();
    },[])

    useEffect(() => {
        setErrMsg('');
    }, [user,pwd])


    // API request
    const handleSubmit = async (e) =>{
        e.preventDefault();
        const userData = {
            email:'asdasd@asdasd.com',
            password:'Jm+-82467913'
        }
        try {
            const response = await axios.post(LOGIN_URL, 
                JSON.stringify(userData),
                {
                    headers:{ 'Content-Type': 'application/json'},
                    withCredentials:true
                }
            )
            const accessToken = response?.data?.accessToken;
            const roles =response?.data?.roles;
            setAuth({user, pwd, roles, accessToken})

            console.log(JSON.stringify(response?.data));
            console.log(JSON.stringify(response));
            
            setPwd('');
            setUser('');
            setSuccess(true);

        } catch (err) {
            console.log(err)
            if (!err?.response) {
                setErrMsg('No Server Response');
            } else if(err.response?.status === 400){
                setErrMsg('Missing username or password')   
            } else if(err.response?.status === 401){
                setErrMsg('Unauthorized')
            } else {
                setErrMsg('Login Failed')
            }
            errRef.current.focus();
        }
        // 
        // Add endpoint
        // 

        
    }

  return (
    <>
    {success ? (
    <section>
        <h1>You are logged in</h1>
        <br/>
        <p>
            <Link to='/'>Go Home</Link>
        </p>
    </section>):(
    <section>
        <p ref={errRef} className={errMsg? "errmsg":"offscreen"} aria-live='assertive'>{errMsg}</p>
        <h1>Sign In</h1>
        <form onSubmit={handleSubmit}>
            <label htmlFor='username'>
                Username:
            </label>
            <input
                type='text'
                id='username'
                ref={userRef}
                autoComplete='off'
                onChange={(e)=>setUser(e.target.value)}
                value={user}
                required
            />
            
            <label htmlFor='password'>
                Password:
            </label>
            <input
                type='password'
                id='password'
                onChange={(e)=>setPwd(e.target.value)}
                value={pwd}
                required
            />
            <button type='submit'>Sign In</button>
            Need an Account? <br/>
            <span className='line'>
                <Link to='/register'>Register</Link>
            </span>
        </form>
    </section>
    )}
    </>
  )
}

export default Login
