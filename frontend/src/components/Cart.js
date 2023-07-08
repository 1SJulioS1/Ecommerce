import "./Cart.css";
import "./CartScripts.js";
import { AiFillStar } from "react-icons/ai";
import { AiOutlineLeft } from "react-icons/ai";

const Cart = () => {
  return (
    <section className=" w-full m-auto">
      <div class="" id="chec-div">
        <div
          class="w-full justify-center right-0 h-full transition-all"
          id="checkout"
        >
          <div class="flex  lg:flex-row flex-col justify-center" id="cart">
            <div
              class="lg:w-1/2 md:w-8/12 w-full lg:px-8 lg:py-14 md:px-6 px-4 md:py-8 py-4  dark:bg-gray-800   lg:h-screen h-auto"
              id="scroll"
            >
              <div
                class="flex items-center text-gray-500 hover:text-gray-600 dark:text-white cursor-pointer"
                onclick="checkoutHandler(false)"
              >
                <AiOutlineLeft />
                <p class="text-sm pl-2 leading-none dark:hover:text-gray-200">
                  Back
                </p>
              </div>
              <p class="lg:text-4xl text-3xl font-black leading-10 text-gray-800 dark:text-white pt-3">
                Cart
              </p>
              {/* Product 1 */}
              <div class="md:flex items-strech py-8 md:py-10 lg:py-8  border-gray-50">
                <div class="md:w-4/12 2xl:w-1/4 w-full ">
                  <img
                    src="https://i.ibb.co/SX762kX/Rectangle-36-1.png"
                    alt="Black Leather Bag"
                    class="h-full object-center rounded-md object-cover md:block hidden"
                  />
                  <img
                    src="https://i.ibb.co/g9xsdCM/Rectangle-37.pngg"
                    alt="Black Leather Bag"
                    class="md:hidden w-full h-full rounded-md object-center object-cover"
                  />
                </div>
                <div class=" md:w-8/12 2xl:w-3/4 flex flex-col justify-center">
                  <p class="text-xs leading-3 text-gray-800 dark:text-white md:pt-0 pt-4">
                    RF293
                  </p>
                  <div class="flex items-center justify-between w-full p-1">
                    <p class=" font-black uppercase w-fit ">North wolf bag</p>
                    <h2 className="w-full text-end p-1 ">Quantity</h2>
                    <select
                      aria-label="Select quantity"
                      class="p-2 border border-gray-200 focus:outline-none cursor-pointer hover:bg-gray-200 focus:bg-gray-200 "
                    >
                      <option>01</option>
                      <option>02</option>
                      <option>03</option>
                    </select>
                  </div>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white pt-2">
                    Height: 10 inches
                  </p>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white py-4">
                    Color: Black
                  </p>
                  <p class=" text-xs leading-3 text-gray-600 dark:text-white">
                    Composition: 100% calf leather
                  </p>
                  <div class="flex items-center justify-between pt-5">
                    <div class="flex gap-3 p-1 content-center ">
                      <div className=" flex hover:bg-yellow-300 rounded-md text-sm bg-yellow-400">
                        <AiFillStar className="self-center ml-1" />
                        <p class="p-1 font-semibold  text-black cursor-pointer">
                          Add to favorites
                        </p>
                      </div>
                      <p
                        class="p-1  text-sm rounded-md hover:bg-red-700 font-semibold
                      bg-red-800 text-white cursor-pointer"
                      >
                        Remove
                      </p>
                    </div>
                    <p class="  font-black">,000</p>
                  </div>
                </div>
              </div>
              {/* Product 2 */}
              <div class="md:flex items-strech py-8 md:py-10 lg:py-8 border-t border-gray-50">
                <div class="md:w-4/12 2xl:w-1/4 w-full">
                  <img
                    src="https://i.ibb.co/c6KyDXN/Rectangle-5-1.png"
                    alt="Gray Sneakers"
                    class="h-full object-center object-cover md:block hidden"
                  />
                  <img
                    src="https://i.ibb.co/yVSpYqx/Rectangle-6.png"
                    alt="Gray Sneakers"
                    class="md:hidden w-full h-full object-center object-cover"
                  />
                </div>
                <div class="md:pl-3 md:w-8/12 2xl:w-3/4 flex flex-col justify-center">
                  <p class="text-xs leading-3 text-gray-800 dark:text-white md:pt-0 pt-4">
                    RF293
                  </p>
                  <div class="flex items-center justify-between w-full pt-1">
                    <p class="text-base font-black leading-none text-gray-800 dark:text-white">
                      LW sneakers
                    </p>
                    <select
                      aria-label="Select quantity"
                      class="py-2 px-1 border border-gray-200 mr-6 focus:outline-none dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-white"
                    >
                      <option>01</option>
                      <option>02</option>
                      <option>03</option>
                    </select>
                  </div>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white pt-2">
                    Height: 10 inches
                  </p>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white py-4">
                    Color: Black
                  </p>
                  <p class="w-96 text-xs leading-3 text-gray-600 dark:text-white">
                    Composition: 100% calf leather
                  </p>
                  <div class="flex items-center justify-between pt-5">
                    <div class="flex itemms-center">
                      <p class="text-xs leading-3 underline text-gray-800 dark:text-white cursor-pointer">
                        Add to favorites
                      </p>
                      <p class="text-xs leading-3 underline text-red-500 pl-5 cursor-pointer">
                        Remove
                      </p>
                    </div>
                    <p class="text-base font-black leading-none text-gray-800 dark:text-white">
                      ,000
                    </p>
                  </div>
                </div>
              </div>
              {/* Product 3 */}
              <div class="md:flex items-strech py-8 md:py-10 lg:py-8 border-t border-gray-50">
                <div class="md:w-4/12 2xl:w-1/4 w-full">
                  <img
                    src="https://i.ibb.co/6gzWwSq/Rectangle-20-1.png"
                    alt="Black Leather Purse"
                    class="h-full object-center object-cover md:block hidden"
                  />
                  <img
                    src="https://i.ibb.co/TTnzMTf/Rectangle-21.png"
                    alt="Black Leather Purse"
                    class="md:hidden w-full h-full object-center object-cover"
                  />
                </div>
                <div class="md:pl-3 md:w-8/12 2xl:w-3/4 flex flex-col justify-center">
                  <p class="text-xs leading-3 text-gray-800 dark:text-white md:pt-0 pt-4">
                    RF293
                  </p>
                  <div class="flex items-center justify-between w-full">
                    <p class="text-base font-black leading-none text-gray-800 dark:text-white">
                      Luxe card holder
                    </p>
                    <select
                      aria-label="Select quantity"
                      class="py-2 px-1 border border-gray-200 mr-6 focus:outline-none dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-white"
                    >
                      <option>01</option>
                      <option>02</option>
                      <option>03</option>
                    </select>
                  </div>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white pt-2">
                    Height: 10 inches
                  </p>
                  <p class="text-xs leading-3 text-gray-600 dark:text-white py-4">
                    Color: Black
                  </p>
                  <p class="w-96 text-xs leading-3 text-gray-600 dark:text-white">
                    Composition: 100% calf leather
                  </p>
                  <div class="flex items-center justify-between pt-5">
                    <div class="flex itemms-center">
                      <p class="text-xs leading-3 underline text-gray-800 dark:text-white cursor-pointer">
                        Add to favorites
                      </p>
                      <p class="text-xs leading-3 underline text-red-500 pl-5 cursor-pointer">
                        Remove
                      </p>
                    </div>
                    <p class="text-base font-black leading-none text-gray-800 dark:text-white">
                      ,000
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="lg:w-96 md:w-8/12 w-full bg-gray-100 dark:bg-gray-900 h-full">
              <div class="flex flex-col lg:h-screen h-auto lg:px-8 md:px-7 px-4 lg:py-20 md:py-10 py-6 justify-between overflow-y-auto">
                <div>
                  <p class="lg:text-4xl text-3xl font-black leading-9 text-gray-800 dark:text-white">
                    Summary
                  </p>
                  <div class="flex items-center justify-between pt-16">
                    <p class="text-base leading-none text-gray-800 dark:text-white">
                      Subtotal
                    </p>
                    <p class="text-base leading-none text-gray-800 dark:text-white">
                      ,000
                    </p>
                  </div>
                  <div class="flex items-center justify-between pt-5">
                    <p class="text-base leading-none text-gray-800 dark:text-white">
                      Shipping
                    </p>
                    <p class="text-base leading-none text-gray-800 dark:text-white"></p>
                  </div>
                  <div class="flex items-center justify-between pt-5">
                    <p class="text-base leading-none text-gray-800 dark:text-white">
                      Tax
                    </p>
                    <p class="text-base leading-none text-gray-800 dark:text-white"></p>
                  </div>
                </div>
                <div>
                  <div class="flex items-center pb-6 justify-between lg:pt-5 pt-20">
                    <p class="text-2xl leading-normal text-gray-800 dark:text-white">
                      Total
                    </p>
                    <p class="text-2xl font-bold leading-normal text-right text-gray-800 dark:text-white">
                      ,240
                    </p>
                  </div>
                  <button
                    onclick="checkoutHandler1(true)"
                    class="text-base leading-none w-full py-5 bg-gray-800 border-gray-800 border focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 text-white dark:hover:bg-gray-700"
                  >
                    Checkout
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Cart;
