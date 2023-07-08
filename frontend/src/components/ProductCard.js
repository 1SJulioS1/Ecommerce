const ProductCard = (props) => {
  return (
    <div className=" aspect-h-1 aspect-w-1 w-full overflow-hidden  rounded-lg bg-gray-200 xl:aspect-h-8 xl:aspect-w-7">
      <img
        src="https://tailwindui.com/img/ecommerce-images/category-page-04-image-card-01.jpg"
        alt="Tall slender porcelain bottle with natural clay textured body and cork stopper."
        className="h-full w-full object-cover object-center group-hover:opacity-75"
      />
      <h3 className="mt-1 ml-3 font-semibold text-left text-sm text-gray-700">
        {props.name}
      </h3>
      <p className="mt-1 ml-3 font-thin text-left text-gray-900">
        {props.description}
      </p>
      <p className=" justify-center mt-1 rounded-tr-xl bg-red-700 w-fit p-1 pr-5 text-2xl font-thin text-white">
        $48
      </p>
    </div>
  );
};

export default ProductCard;
