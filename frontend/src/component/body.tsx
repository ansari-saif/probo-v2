import { TopStories } from "./topStories";
import download from "../assets/downloadapp.avif";
import { symbols } from "../db/data";
import { TradeCard } from "./tradCard";
import tshirt from "../assets/Tshirt.avif";
import { Download } from "./download";
import { useState } from "react";

export const BodyContent = () => {
  const [isDownload, setIsDownload] = useState(false)
  return (
    <>
      <div className="p-4 relative px-10 flex">

        <div className="lg:w-[70%] w-[100%] ">
          <h1 className="text-xl font-semibold mb-3">Top Stories</h1>
          <TopStories />
          <div id="allevents" className="pt-4">
            <h1 className="text-xl font-semibold mb-3">All events</h1>
            <hr />

            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              {symbols.map((symbol) => (
                <TradeCard
                  symbol={symbol}
                  url={symbol.url}
                  yesPrice={symbol.yesPrice}
                  noPrice={symbol.noPrice}
                  totalTrades={symbol.traders}
                  title={symbol.title}
                  description={symbol.description}
                />
              ))}
            </div>
          </div>
        </div>
        <div key="add" className="w-[30%] ml-8 hidden lg:block">
          <div className="rounded-lg p-4 justify-around bg-[#EDEDED] mt-5 flex">
            <div className="w-1/2">
              <h1 className="text-xl font-bold ">
                DOWNLOAD APP FOR BETTER & FAST EXPERIENCE
              </h1>
              <button onClick={()=> setIsDownload(true)} className="bg-black text-sm mt-2 px-10 p-2 rounded text-white font-medium">
                Download Now
              </button>
            </div>
            <img
              className="object-contain"
              width={100}
              height={100}
              src={download}
              alt="download"
            />
          </div>
          <h1 className="font-bold text-xl mt-4">Featured Stories</h1>
          <div className="rounded-lg p-4 flex bg-[#EDEDED] mt-5 cursor-pointer">
            <img
              className="rounded-lg object-contain"
              width={80}
              height={60}
              src={tshirt}
              alt="tshirt"
            />
            <div className="ml-4">
              <h2 className="text-[#165BB7] font-semibold">Cricket</h2>
              <p className="font-semibold w-[70%] text-sm">
                Pakistan to win the 2nd Test vs Bangladesh?
              </p>
              <span className="text-xs font-thin text-[#262626]">
                October 25th 2024
              </span>
            </div>
          </div>
        </div>
      </div>

      {isDownload && <Download setIsDownload={setIsDownload} />}
    </>
  );
};
