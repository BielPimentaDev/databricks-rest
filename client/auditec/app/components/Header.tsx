"use client";
import { ChevronUp, SlidersHorizontal } from "lucide-react";
import { useDataStore, useParamsStore } from "../store/useStore";
import { useState } from "react";

export const Header = () => {
  const [isFilterOpen, setIsFilterOpen] = useState<boolean>(false);
  const { setQueryParam, queryParam } = useParamsStore();
  const [selectedValue, setSelectedValue] = useState("");
  const { dataStore } = useDataStore();
  const handleChange = (event) => {
    setSelectedValue(event.target.value);
    console.log(selectedValue);
  };

  const onSliderClick = () => {
    setIsFilterOpen((prev) => !prev);
  };
  const onSend = () => {
    setQueryParam(selectedValue);
    setIsFilterOpen((prev) => !prev);
  };

  return (
    <>
      <header className="bg-white shadow-md z-20     mb-8 fixed top-0 w-full transition-max-height duration-300 ease-in-out">
        <div className="max-w-[2000px] p-5 px-8 mx-auto ">
          <div className="flex  w-full">
            <button onClick={onSliderClick} className="mr-4">
              <SlidersHorizontal className="cursor-pointer" size={24} />
            </button>
            <div className="flex gap-4 justify-between w-full items-center">
              <div className="flex items-center">
                <select
                  id=""
                  name=""
                  className="block w-full  cursor-pointer border-gray-300 rounded-md  shadow-sm border-none p-2  font-semibold  text-lg "
                >
                  <option value="all" selected>
                    Mes : junho, 09/24/2024, 02:57:42 PM
                  </option>
                </select>
              </div>

              <div className="flex  gap-4">
                <div className="flex items-center bg-red-500/20 p-1  px-2 text-sm  rounded-full text-red-500">
                  <span className=" font-bold ">19 </span>
                  <p className="pl-1">fundos </p>
                </div>
                <div className="flex items-center bg-green-600/20 p-1 px-2  text-sm rounded-full text-green-600">
                  <span className=" font-bold ">27 </span>
                  <p className="pl-1">fundos </p>
                </div>
              </div>
            </div>
          </div>
          {queryParam && (
            <div className="mt-4 flex gap-4 ">
              <div>
                <p className="text-red-500 font- border text-sm px-4 py-1 border-red-500 rounded-full  self-start">
                  {queryParam}
                </p>
              </div>

              <div className="flex gap-2 ">
                <p className="font-semibold mb-2 flex ">Total:</p>
                <p>{dataStore.total_batimentos}</p>
              </div>
            </div>
          )}
          {isFilterOpen && (
            <div className="mt-6 flex-col flex  items-start">
              <div>
                <label>Filtrar por erro:</label>
                <select
                  id="frutas"
                  name="frutas"
                  onChange={handleChange}
                  className="cursor-pointer ml-4 bg-slate-200 p-1 rounded-full"
                >
                  <option value="attributeError">Attribute Error</option>
                  <option value="IndexError">Index Error</option>
                  <option value="[UNRESOLVED_COLUMN">Unresolved Column</option>
                  <option value="">Todos</option>
                </select>
              </div>
              <button
                onClick={onSend}
                type="submit"
                value="Enviar"
                className="bg-purple-500 text-white px-12 py-1 mt-12 rounded-full"
              >
                Enviar
              </button>
              <button
                className="absolute left-1/2 -bottom-2 p-1 bg-white rounded-full"
                onClick={onSliderClick}
              >
                <ChevronUp size={24} />
              </button>
            </div>
          )}
        </div>
      </header>
      {isFilterOpen && (
        <div className="fixed w-screen h-screen bg-zinc-700/40 "></div>
      )}
    </>
  );
};
