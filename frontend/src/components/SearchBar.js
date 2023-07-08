import { MdOutlineSearch } from "react-icons/md";

const SearchBar = () => {
  return (
    <div class=" self-center">
      <form className="">
        <label
          for="default-search"
          class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300"
        >
          Search
        </label>
        <div class="relative overflow-hidden group ">
          <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
            <MdOutlineSearch className="w-5 h-5 absolute text-black group-hover:text-red-800 transition-all" />
          </div>
          <input
            type="search"
            id="default-search"
            class=" px-8 text-sm rounded-3xl border border-gray-300 bg-white py-2 focus:shadow-lg focus:pr-20 placeholder-gray-400  focus:text-black self-center transition-all"
            required
          />
          <button
            type="submit"
            class="text-white absolute right-0 bottom-0 bg-black hover:bg-yellow-400 hover:text-black focus:ring-4 focus:outline-none  font-medium rounded-r-full text-sm px-3 h-full text-center "
          >
            Search
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchBar;
