import { useState, useRef, useEffect } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import axios from "../api/axios";

const Login = () => {
  const { setAuth } = useAuth();

  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from.pathname || "/";

  const userRef = useRef();
  const errRef = useRef();

  const [email, setEmail] = useState("");
  const [password, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "api/login/",
        JSON.stringify({ email, password }),
        {
          headers: { "Content-Type": "application/json" },
          // withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.access;
      const refreshToken = response?.data?.refresh;
      // const roles = response?.data?.roles;
      console.log(accessToken);
      setAuth({
        accessToken: accessToken,
        roles: "2001",
        refreshToken: refreshToken,
      });
      setEmail("");
      setPwd("");
      navigate(from, { replace: true });
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <div className="bg-black">
      {/* {success ? (
        <div>
          <h1>You are logged in</h1>
          <br />
          <p>
            <Link to="/">Go Home</Link>
          </p>
        </div>
      ) : ( */}
      <div className="flex min-h-full py-10 flex-1 flex-col justify-center px-6 lg:px-8 sm:mx-auto sm:w-full sm:max-w-sm">
        <p
          ref={errRef}
          className={errMsg ? "errmsg" : "offscreen"}
          aria-live="assertive"
        >
          {errMsg}
        </p>

        <h2 className="mt-10 text-center text-2xl font-bold tracking-tight text-gray-900 mb-3">
          Sign in to your account
        </h2>

        <form
          onSubmit={handleSubmit}
          className=" space-y-3 p-6 glass rounded-lg"
        >
          <label
            htmlFor="email"
            className="block text-sm font-medium text-gray-900 text-left"
          >
            Email:
          </label>

          <input
            className="p-1 rounded-lg focus-visible:border-cyan-600  w-full transition-all"
            type="email"
            id="email"
            ref={userRef}
            autoComplete="off"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            placeholder="Ex: example@gmail.com "
            required
          />

          <label
            htmlFor="password"
            className="block text-sm font-medium text-gray-900 text-left"
          >
            Password:
          </label>

          <input
            className="p-1 rounded-lg focus-visible:border-cyan-600 w-full transition-all"
            type="password"
            id="password"
            onChange={(e) => setPwd(e.target.value)}
            value={password}
            placeholder="Type your password here"
            required
          />
          {/*
             {Link to forgot Password page} 
            */}
          <a
            href="/"
            className="text-right font-semibold text-indigo-600 hover:text-indigo-500 block"
          >
            Forgot password?
          </a>

          <button
            type="submit"
            className="flex w-full  justify-center rounded-md bg-indigo-600 p-3 text-sm font-semibold  text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>

          <h2>You do not have an account?</h2>
          <Link
            className=" underline text-cyan-700 active:text-black"
            to="/register"
          >
            Register here
          </Link>
        </form>
      </div>
    </div>
  );
};

export default Login;
