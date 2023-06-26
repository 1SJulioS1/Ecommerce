import { useRef, useState, useEffect } from "react";
import './RegisterFormStyles.css'
// import axios from '../api/axios';

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*/+-.,]).{8,24}$/;
const REGISTER_URL = '/register';
const email = '123@123.com';
const phone = +5355742168;



const Register = () => {
    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');
    const [validName, setValidName] = useState(false);
    const [userFocus, setUserFocus] = useState(false);

    const [pwd, setPwd] = useState('');
    const [validPwd, setValidPwd] = useState(false);
    const [pwdFocus, setPwdFocus] = useState(false);

    const [matchPwd, setMatchPwd] = useState('');
    const [validMatch, setValidMatch] = useState(false);
    const [matchFocus, setMatchFocus] = useState(false);

    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setValidName(USER_REGEX.test(user));
    }, [user])

    useEffect(() => {
        setValidPwd(PWD_REGEX.test(pwd));
        setValidMatch(pwd === matchPwd);
    }, [pwd, matchPwd])

    useEffect(() => {
        setErrMsg('');
    }, [user, pwd, matchPwd])
        
    const handleSubmit = async (e) => {
        e.preventDefault();
        // if button enabled with JS hack
        const v1 = USER_REGEX.test(user);
        const v2 = PWD_REGEX.test(pwd);
        if (!v1 || !v2) {
            setErrMsg("Invalid Entry");
            return;
        }
        try {
            fetch('http://127.0.0.1:8000/api/users/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username:'3duser', password:'1359879', email:'3rd@email.com', phone:'+5355664488'} ), // Replace with your data object
            })
            .then(response => {
                console.log(response)
            if (!response.ok) {
            throw new Error('Network response was not OK');
            }
            return response.json();
            })
            .then(data => {
            // Handle the response data
            console.log(data);
            })
            .catch(error => {
            // Handle any errors
            console.error('Error:', error);
            });
    
        } catch (error) {
            console.log(error)
        }
        setSuccess(true);
        

        

        // try {
        //     const response = await axios.post(REGISTER_URL,
        //         JSON.stringify({ user, pwd }),
        //         {
        //             headers: { 'Content-Type': 'application/json' },
        //             withCredentials: true,
        //             username:{user},
        //             password:{pwd}
                    

        //         }
        //     );
        //     console.log(response?.data);
        //     console.log(response?.accessToken);
        //     console.log(JSON.stringify(response))
        //     setSuccess(true);
        //     //clear state and controlled inputs
        //     //need value attrib on inputs for this
        //     setUser('');
        //     setPwd('');
        //     setMatchPwd('');
        // } catch (err) {
        //     if (!err?.response) {
        //         setErrMsg('No Server Response');
        //     } else if (err.response?.status === 409) {
        //         setErrMsg('Username Taken');
        //     } else {
        //         setErrMsg('Registration Failed')
        //     }
        //     errRef.current.focus();
        // }
    }

    return (
        <>
            {success ? (
                <section>
                    <h1>Success!</h1>
                    <p>
                        <a href="#">Sign In</a>
                    </p>
                </section>
            ) : (
                <section>
                    <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1>Register</h1>
                    <form onSubmit={handleSubmit}>
                        <label htmlFor="username">
                            Username:
                        </label>
                        <input
                            type="text"
                            id="username"
                            ref={userRef}
                            autoComplete="off"
                            onChange={(e) => {setUser(e.target.value); console.log({validName})}}
                            value={user}
                            required
                            aria-invalid={validName ? "false" : "true"}
                            aria-describedby="uidnote"
                            onFocus={() => setUserFocus(true)}
                            onBlur={() => setUserFocus(false)}
                        />
                        <p id="uidnote" className={userFocus && user && !validName ? "instructions" : "offscreen"}>
                            4 to 24 characters.<br />
                            Must begin with a letter.<br />
                            Letters, numbers, underscores, hyphens allowed.
                        </p>


                        <label htmlFor="password">
                            Password:
                            
                        </label>
                        <input
                            type="password"
                            id="password"
                            onChange={(e) => {setPwd(e.target.value); console.log(validPwd)}}
                            value={pwd}
                            required
                            aria-invalid={validPwd ? "false" : "true"}
                            aria-describedby="pwdnote"
                            onFocus={() => setPwdFocus(true)}
                            onBlur={() => setPwdFocus(false)}
                        />
                        <p id="pwdnote" className={pwdFocus && !validPwd ? "instructions" : "offscreen"}>
                            
                            8 to 24 characters.<br />
                            Must include uppercase and lowercase letters, a number and a special character.<br />
                            Allowed special characters: <span >!@#$%^&*/+-.,</span>
                        </p>


                        <label htmlFor="confirm_pwd">
                            Confirm Password:
                            
                        </label>
                        <input
                            type="password"
                            id="confirm_pwd"
                            onChange={(e) => {setMatchPwd(e.target.value); console.log(validMatch)}}
                            value={matchPwd}
                            required
                            aria-invalid={validMatch ? "false" : "true"}
                            aria-describedby="confirmnote"
                            onFocus={() => setMatchFocus(true)}
                            onBlur={() => setMatchFocus(false)}
                        />
                        <p id="confirmnote" className={matchFocus && !validMatch ? "instructions" : "offscreen"}>
                            
                            Must match the first password input field.
                        </p>

                        <button disabled={!validName || !validPwd || !validMatch ? true : false}>Sign Up</button>
                    </form>
                    <p>
                        Already registered?<br />
                        <span className="line">
                            {/*put router link here*/}
                            <a href="#">Sign In</a>
                        </span>
                    </p>
                </section>
            )}
        </>
    )
}

export default Register