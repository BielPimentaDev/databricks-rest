"use client";
import { useEffect, useState } from "react";
import axios from "axios";

import { useDataStore, useParamsStore } from "./store/useStore";
export default function Home() {
  const [data, setData] = useState([]);
  const { queryParam } = useParamsStore();
  const { setDataStore } = useDataStore();
  useEffect(() => {
    const fetchAPI = async () => {
      try {
        const url = `http://127.0.0.1:5000/api?error_parameter=${queryParam}`;
        console.log(url);
        const response = await axios.get(url);

        setData(response.data[0].fundos);
        setDataStore(response.data[0]);
      } catch (err) {
        console.error(err);
      }
    };

    fetchAPI();
  }, [queryParam]);

  return (
    <main className="py-12 px-4 max-w-[1500px] mx-auto bg-zinc-50">
      <div className="mt-20 grid-cols-1 grid gap-2 gap-y-2  mx-16 ">
        {data.map((item, index) => {
          return (
            <div key={index} className="py-2 flex flex-col">
              <h2 className="font-semibold text-lg mb-2 border-b-2 border-zinc-200 pb-2 p-2 pl-4">
                {item.fundo}
              </h2>
              <div className=" flex  flex-col text-sm">
                {item.batimentos.map((item, index) => {
                  return (
                    <a key={index} href={item.link} target="_blank">
                      <div className="flex gap-3 py-4 px-2 items-start hover:bg-zinc-200/50 cursor-pointer">
                        <p className="p-1 rounded-full px-6 text-white bg-purple-500 min-w-36 text-center">
                          {item.batimento}
                        </p>
                        <p className="text-sm">{item.erro} </p>
                      </div>
                    </a>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </main>
  );
}
