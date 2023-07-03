import "./BottomNavBarStyles.css";
// import React from 'react'
import { NavLink } from "react-router-dom";
import { BiCategoryAlt } from "react-icons/bi";

// const BottomNavBar = () => {
//   return (
//     <div>
//       <nav className='bottom-nav-bar'>
//         <ul>
//           <li>
//         <NavLink to='/'>
//           <span className="material-symbols-rounded">home</span>
//           Home
//         </NavLink>
//         </li>
//         <li>
//         <NavLink to='user'><span className="material-symbols-rounded">person</span>
//           User
//         </NavLink>
//         </li>
//         <li>
//         <NavLink to='cart'><span className="material-symbols-rounded">shopping_cart</span>
//           Cart
//         </NavLink>
//         </li>
//         <li>
//         <NavLink to='orders'><span className="material-symbols-rounded">fact_check</span>
//           Orders
//         </NavLink>
//         </li>
// </ul>
//       </nav>
//     </div>
//   )
// }

// export default BottomNavBar

import { Fragment } from "react";
import { Disclosure, Menu, Transition } from "@headlessui/react";
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/react/24/outline";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}
const navigation = [
  { name: "Home", href: "/", current: true },
  { name: "User", href: "/user", current: false },
  { name: "Cart", href: "/cart", current: false },
  { name: "Orders", href: "/orders", current: false },
];

export default function BottomNavBar({ switchSideNav }) {
  return (
    <Disclosure as="nav" className="bg-red-800 shadow-xl">
      {({ open }) => (
        <>
          <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div className="relative flex h-16 items-center justify-between">
              <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
                {/* Mobile menu button*/}
                <Disclosure.Button className="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
                  <span className="sr-only">Open main menu</span>
                  {open ? (
                    <XMarkIcon className="block h-6 w-6" aria-hidden="true" />
                  ) : (
                    <Bars3Icon className="block h-6 w-6" aria-hidden="true" />
                  )}
                </Disclosure.Button>
                <button
                  className="text-gray-300 flex gap-2 content-end hover:bg-gray-700 hover:text-white
                          rounded-md px-3 py-2 text-sm font-medium transition-all bg-red-950  p-3 "
                  onClick={switchSideNav}
                >
                  <BiCategoryAlt className=" self-center" />
                  <h2>Categories</h2>
                </button>
              </div>
              <div className="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                <div className="flex flex-shrink-0 items-center">
                  <img
                    className="block h-8 w-auto lg:hidden "
                    src={process.env.PUBLIC_URL + "/icons8-logo.svg"}
                    alt="Torresuelto"
                  />
                  <img
                    className="hidden h-8 w-20  lg:block bg-white rounded-full scale-125 p-1   "
                    src={process.env.PUBLIC_URL + "/icons8-logo.svg"}
                    alt="Torresuelto"
                  />
                </div>
                <div className="hidden sm:ml-6 sm:block">
                  <div className="flex justify-center content-center space-x-4 ">
                    <button
                      className="text-gray-300 flex gap-2 content-end hover:bg-gray-700 hover:text-white
                          rounded-md px-3 py-2 text-sm font-medium transition-all bg-red-950  p-3 "
                      onClick={switchSideNav}
                    >
                      <BiCategoryAlt className=" self-center" />
                      <h2>Categories</h2>
                    </button>
                    {navigation.map((item) => (
                      <NavLink
                        to={item.href}
                        key={item.name}
                        className={classNames(
                          "text-gray-300 hover:bg-gray-700 hover:text-white",
                          "rounded-md px-3 py-2 text-sm font-medium transition-all"
                        )}
                        aria-current={item.current ? "page" : undefined}
                      >
                        {item.name}
                      </NavLink>
                    ))}
                  </div>
                </div>
              </div>
              <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                <button
                  type="button"
                  className="rounded-full bg-red-800 p-1 text-gray-700 hover:text-yellow-500 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                >
                  <span className="sr-only">View notifications</span>
                  <BellIcon
                    className="h-6 transition-all w-6"
                    aria-hidden="true"
                  />
                </button>

                {/* Profile dropdown */}
                <Menu as="div" className="relative ml-3">
                  <div>
                    <Menu.Button className=" flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                      <span className="sr-only">Open user menu</span>
                      <img
                        className="h-8 w-8 rounded-full"
                        src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                        alt=""
                      />
                    </Menu.Button>
                  </div>
                  <Transition
                    as={Fragment}
                    enter="transition ease-out duration-100"
                    enterFrom="transform opacity-0 scale-95"
                    enterTo="transform opacity-100 scale-100"
                    leave="transition ease-in duration-75"
                    leaveFrom="transform opacity-100 scale-100"
                    leaveTo="transform opacity-0 scale-95"
                  >
                    <Menu.Items className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                      <Menu.Item>
                        {({ active }) => (
                          <a
                            href="#"
                            className={classNames(
                              active ? "bg-gray-100" : "",
                              "block px-4 py-2 text-sm text-gray-700"
                            )}
                          >
                            Your Profile
                          </a>
                        )}
                      </Menu.Item>
                      <Menu.Item>
                        {({ active }) => (
                          <a
                            href="#"
                            className={classNames(
                              active ? "bg-gray-100" : "",
                              "block px-4 py-2 text-sm text-gray-700"
                            )}
                          >
                            Settings
                          </a>
                        )}
                      </Menu.Item>
                      <Menu.Item>
                        {({ active }) => (
                          <a
                            href="#"
                            className={classNames(
                              active ? "bg-gray-100" : "",
                              "block px-4 py-2 text-sm text-gray-700"
                            )}
                          >
                            Sign out
                          </a>
                        )}
                      </Menu.Item>
                    </Menu.Items>
                  </Transition>
                </Menu>
              </div>
            </div>
          </div>

          <Disclosure.Panel className="sm:hidden">
            <div className="space-y-1 px-2 pb-3 pt-2">
              {navigation.map((item) => (
                <Disclosure.Button
                  key={item.name}
                  as="a"
                  href={item.href}
                  className={classNames(
                    item.current
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white",
                    "block rounded-md px-3 py-2 text-base font-medium"
                  )}
                  aria-current={item.current ? "page" : undefined}
                >
                  {item.name}
                </Disclosure.Button>
              ))}
            </div>
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  );
}
