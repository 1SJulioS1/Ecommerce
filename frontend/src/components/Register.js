import { useRef, useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Register.css";

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*/+-.,]).{8,24}$/;
const EMAIL_REGEX = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
const PHONE_REGEX = /^5\d{7}$/;

const Register = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [validName, setValidName] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [email, setEmail] = useState("");
  const [validEmail, setValidEmail] = useState(false);
  const [emailFocus, setEmailFocus] = useState(false);

  const [phoneNumber, setPhoneNumber] = useState("");
  const [validPhoneNumber, setValidPhoneNumber] = useState(false);
  const [phoneNumberFocus, setPhoneNumberFocus] = useState(false);

  const [pwd, setPwd] = useState("");
  const [validPwd, setValidPwd] = useState(false);
  const [pwdFocus, setPwdFocus] = useState(false);

  const [matchPwd, setMatchPwd] = useState("");
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);

  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setValidName(USER_REGEX.test(user));
  }, [user]);

  useEffect(() => {
    setValidEmail(EMAIL_REGEX.test(email));
  }, [email]);

  useEffect(() => {
    setValidPhoneNumber(PHONE_REGEX.test(phoneNumber));
  }, [phoneNumber]);

  useEffect(() => {
    setValidPwd(PWD_REGEX.test(pwd));
    setValidMatch(pwd === matchPwd);
  }, [pwd, matchPwd]);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd, matchPwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const userData = {
      email: email,
      phone: `+53${phoneNumber}`,
      password: pwd,
      username: user,
    };
    // if button enabled with JS hack
    const v1 = USER_REGEX.test(user);
    const v2 = PWD_REGEX.test(pwd);
    const v3 = EMAIL_REGEX.test(email);
    const v4 = PHONE_REGEX.test(phoneNumber);
    console.log(userData);
    if (!v1 || !v2 || !v3 || !v4) {
      setErrMsg("Invalid Entry");
      return;
    }

    try {
      fetch("http://127.0.0.1:8000/api/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData), // Replace with your data object
      })
        .then((response) => {
          console.log(response);
          if (response.ok) {
            setSuccess(true);
          } else if (!response.ok) {
            throw new Error("Network response was not OK");
          }
          return response.json();
        })
        .then((data) => {
          // Handle the response data
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
          if (!err?.response) {
            setErrMsg("No Server Response");
          } else if (err.response?.status === 409) {
            setErrMsg("Username Taken");
          } else {
            setErrMsg("Registration Failed");
          }
          errRef.current.focus();
        });
      // Handle any errors
      setPhoneNumber("");
      setEmail("");
      setUser("");
      setPwd("");
      setMatchPwd("");
      setSuccess(true);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="  magicpattern h-screen">
      {success ? (
        <section>
          <h1>Success!</h1>
          <p>
            <Link to="/login">Log in</Link>
          </p>
        </section>
      ) : (
        <div className="flex pt-20 h-full w-full flex-col lg:px-0 sm:mx-auto sm:w-full sm:max-w-sm">
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <form
            onSubmit={handleSubmit}
            className=" space-y-7 py-10 mt-10 px-8 glass rounded-lg "
          >
            <h2
              className=" 
        text-black scale-125 text-center text-2xl font-bold tracking-tight  mb-3"
            >
              Register
            </h2>
            <div className="group">
              <label
                htmlFor="username"
                className="block text-sm group-hover:ml-[10%] group-hover:scale-125 transition-all font-medium text-gray-900 text-left"
              >
                Username:
              </label>
              <input
                type="text"
                id="username"
                className="p-1 
               border  border-black rounded-lg w-full transition-all"
                ref={userRef}
                autoComplete="off"
                onChange={(e) => {
                  setUser(e.target.value);
                  console.log({ validName });
                }}
                value={user}
                required
                aria-invalid={validName ? "false" : "true"}
                aria-describedby="uidnote"
                onFocus={() => setUserFocus(true)}
                onBlur={() => setUserFocus(false)}
              />
              <p
                id="uidnote"
                className={
                  userFocus && user && !validName ? "instructions" : "offscreen"
                }
              >
                4 to 24 characters.
                <br />
                Must begin with a letter.
                <br />
                Letters, numbers, underscores, hyphens allowed.
              </p>
            </div>
            <div className="group">
              <label
                htmlFor="email"
                className="group-hover:ml-[10%] transition-all group-hover:scale-125 block text-sm font-medium text-gray-900 text-left"
              >
                Email:
              </label>
              <input
                className="p-1 
            border border-black
            rounded-lg focus-visible:border-cyan-600 w-full transition-all"
                type="email"
                id="email"
                ref={userRef}
                autoComplete="off"
                onChange={(e) => {
                  setEmail(e.target.value);
                  console.log({ validEmail });
                }}
                value={email}
                required
                aria-invalid={validEmail ? "false" : "true"}
                aria-describedby="uidnote"
                onFocus={() => setEmailFocus(true)}
                onBlur={() => setEmailFocus(false)}
              />

              <p
                id="uidnote"
                className={
                  emailFocus && email && !validEmail
                    ? "instructions"
                    : "offscreen"
                }
              >
                Must be a correct email address
                <br />
              </p>
            </div>
            <div className="group flex">
              <label
                htmlFor="phone"
                className=" transition-all group-hover:scale-125 block text-sm font-medium text-gray-900 text-left"
              >
                Phone Number
              </label>
              <h1 className=" scale-125 self-center font-bold pr-3">+53</h1>
              <input
                className="p-1 
            border border-black
            rounded-lg focus-visible:border-cyan-600 w-full transition-all"
                type="number"
                id="phone"
                ref={userRef}
                autoComplete="off"
                onChange={(e) => {
                  setPhoneNumber(e.target.value);
                  console.log({ validPhoneNumber });
                }}
                value={phoneNumber}
                required
                aria-invalid={validPhoneNumber ? "false" : "true"}
                aria-describedby="uidnote"
                onFocus={() => setPhoneNumberFocus(true)}
                onBlur={() => setPhoneNumberFocus(false)}
              />
            </div>
            <p
              id="uidnote"
              className={
                phoneNumberFocus && phoneNumber && !validPhoneNumber
                  ? "instructions"
                  : "offscreen"
              }
            >
              Must not include the prefix
              <br />
            </p>
            <div className="group">
              <label
                htmlFor="password"
                className="group-hover:ml-[10%] transition-all group-hover:scale-125 block text-sm font-medium text-gray-900 text-left"
              >
                Password:
              </label>
              <input
                className="p-1 
            border border-black
            rounded-lg focus-visible:border-cyan-600 w-full transition-all"
                type="password"
                id="password"
                onChange={(e) => {
                  setPwd(e.target.value);
                  console.log(validPwd);
                }}
                value={pwd}
                required
                aria-invalid={validPwd ? "false" : "true"}
                aria-describedby="pwdnote"
                onFocus={() => setPwdFocus(true)}
                onBlur={() => setPwdFocus(false)}
              />
              <p
                id="pwdnote"
                className={pwdFocus && !validPwd ? "instructions" : "offscreen"}
              >
                8 to 24 characters.
                <br />
                Must include uppercase and lowercase letters, a number and a
                special character.
                <br />
                Allowed special characters: <span>!@#$%^&*/+-.,</span>
              </p>
            </div>
            <div className="group">
              <label
                htmlFor="confirm_pwd"
                className="group-hover:ml-[10%] transition-all group-hover:scale-125 block text-sm font-medium text-gray-900 text-left"
              >
                Confirm Password:
              </label>
              <input
                className="p-1 
              border border-black
              rounded-lg focus-visible:border-cyan-600 w-full transition-all"
                type="password"
                id="confirm_pwd"
                onChange={(e) => {
                  setMatchPwd(e.target.value);
                  console.log(validMatch);
                }}
                value={matchPwd}
                required
                aria-invalid={validMatch ? "false" : "true"}
                aria-describedby="confirmnote"
                onFocus={() => setMatchFocus(true)}
                onBlur={() => setMatchFocus(false)}
              />
              <p
                id="confirmnote"
                className={
                  matchFocus && !validMatch ? "instructions" : "offscreen"
                }
              >
                Must match the first password input field.
              </p>
            </div>
            <button
              className="flex w-full  justify-center rounded-md bg-black p-3 text-sm font-semibold  text-white shadow-sm uppercase hover:bg-indigo-800 transition-all border border-[indigo] hover:shadow-lg focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              disabled={
                !validName ||
                !validPwd ||
                !validMatch ||
                !validEmail ||
                !validPhoneNumber
                  ? true
                  : false
              }
            >
              Sign Up
            </button>
            <p>
              Already registered?
              <br />
              <span className="line">
                <Link
                  className=" underline
                w-full  
                font-semibold
                float-left
                active:text-black
                text-indigo-600 hover:text-indigo-500"
                  to="/login"
                >
                  Sign In
                </Link>
              </span>
            </p>
          </form>
        </div>
      )}
    </div>
  );
};

export default Register;
