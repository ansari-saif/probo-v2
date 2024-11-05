import logo from "../assets/probo.avif";
import profile from "../assets/profile.avif";
import { GoHome, GoHomeFill } from "react-icons/go";
import {
  IoBagRemoveOutline,
  IoBagRemove,
  IoWalletOutline,
} from "react-icons/io5";
import { MdKeyboardArrowDown } from "react-icons/md";
import { LuLogOut } from "react-icons/lu";
import { useState } from "react";

export const Navbar = () => {
  const [showLogout, setShowLogout] = useState(false);
  return (
    <>
      <div className="p-6 sticky top-0 z-10 bg-[#F5F5F5] pb-0">
        <div className="border-b border-b-[#E3E3E3] flex justify-between">
          <div className="">
            <img className="" width={100} height={10} src={logo} alt="logo" />
          </div>
          <div className="w-fit gap-10 flex px-4 -mt-4 items-center">
            <span className="cursor-pointer hidden md:block">
              <GoHome size={25} />
            </span>
            <span className="cursor-pointer hidden md:block">
              <IoBagRemoveOutline size={25} />
            </span>
            <button className="border-[1px] p-3 h-10 w-28 rounded flex items-center justify-around cursor-pointer">
              <span>
                <IoWalletOutline />
              </span>
              <span className="font-bold text-sm -mt-[1px]">₹0</span>
            </button>
            <span className="mt-2 h-12 flex">
              <img
                className="mb-4 ml-2 w-10 h-10 rounded-[50%] object-fill"
                // width={50}
                // height={50}
                src={profile}
                alt="profile"
              />
              <span
                onMouseEnter={() => setShowLogout(!showLogout)}
                className="mt-2 ml-2 cursor-pointer"
              >
                <MdKeyboardArrowDown size={25} />
              </span>
            </span>
          </div>
        </div>
        {showLogout && (
          <div className="w-44 z-10 absolute right-12 shadow-lg rounded-lg bg-white p-3 border flex font-mono text-md gap-4 cursor-pointer ">
            <LuLogOut size={25} /> Logout
          </div>
        )}
      </div>
    </>
  );
};
