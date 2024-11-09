import { useState } from "react";
import LoginModel from "./loginModel"
import { Home, Briefcase, Wallet, ChevronDown, Settings, LogOut, User } from 'lucide-react';

const checkIsLoggedIn = () => {
    return localStorage.access_token
}
const Header = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);


    return (
        <div className="flex items-center justify-between bg-gray-100 px-6 py-2 border-b border-gray-200">
            <LoginModel isOpen={isOpen} setIsOpen={setIsOpen} />
            {/* Left side: Logo and links */}
            <div className="flex items-center space-x-8">
                {/* Logo */}
                <img
                    src="https://probo.in/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo.f2d033c9.webp&w=256&q=75"
                    alt="Probo Logo"
                    className="h-8 w-auto" />

                {/* Links */}
                <nav className="flex space-x-6 text-gray-700">
                    <a href="#" className="hover:text-black">Trading</a>
                    <a href="#" className="hover:text-black">Team 11</a>
                    <a href="#" className="hover:text-black">Read</a>
                    <a href="#" className="hover:text-black">Cares</a>
                    <a href="#" className="hover:text-black">Careers</a>
                </nav>
            </div>

            {/* Right side: Notice, buttons, and language icon */}
            {
                !checkIsLoggedIn() ? <>
                    <div className="flex items-center space-x-4">
                        <span className="text-gray-600 text-sm">For 18 years and above only</span>

                        {/* Download App button */}
                        <button className="px-4 py-1 border border-gray-300 text-gray-800 rounded hover:bg-gray-200">
                            Download App
                        </button>

                        {/* Login/Signup button */}
                        <button className="px-4 py-1 bg-gray-800 text-white rounded hover:bg-gray-700" onClick={() => setIsOpen(true)}>
                            Login/Signup
                        </button>

                        {/* Language icon (Assuming this is a language icon) */}
                        <div className="text-gray-600">
                            {/* Placeholder for language icon */}
                            <span className="material-icons">translate</span>
                        </div>
                    </div>
                </> :
                    <div className="flex gap-2 justify-center items-center gap-4">
                        <div className="flex items-center space-x-6">
                            <a
                                href="/"
                                className="flex items-center space-x-2 text-gray-700 hover:text-gray-900 transition-colors"
                            >
                                <Home className="w-5 h-5" />
                                <span className="font-medium">Home</span>
                            </a>

                            <a
                                href="/portfolio"
                                className="flex items-center space-x-2 text-gray-700 hover:text-gray-900 transition-colors"
                            >
                                <Briefcase className="w-5 h-5" />
                                <span className="font-medium">Portfolio</span>
                            </a>
                        </div>

                        {/* Center section */}
                        <div className="flex items-center">
                            <button className="flex items-center space-x-2 px-4 py-1.5 bg-gray-100 rounded-md hover:bg-gray-200 transition-colors">
                                <Wallet className="w-4 h-4 text-gray-600" />
                                <span className="text-gray-900 font-medium">₹13</span>
                            </button>
                        </div>

                        {/* Right section - Custom Dropdown */}
                        <div className="relative">
                            <button
                                onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                                className="flex items-center space-x-2 hover:opacity-80 transition-opacity"
                            >
                                <div className="w-8 h-8 bg-gray-200 rounded-full" />
                                <ChevronDown className="w-4 h-4 text-gray-600" />
                            </button>

                            {isDropdownOpen && (
                                <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                                    <div className="py-1">
                                        <button
                                            className="flex w-full items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                            onClick={() => setIsDropdownOpen(false)}
                                        >
                                            <User className="w-4 h-4 mr-2" />
                                            Profile
                                        </button>
                                        <button
                                            className="flex w-full items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                            onClick={() => setIsDropdownOpen(false)}
                                        >
                                            <Settings className="w-4 h-4 mr-2" />
                                            Settings
                                        </button>
                                        <button
                                            className="flex w-full items-center px-4 py-2 text-sm text-red-500 hover:bg-gray-100 hover:text-red-600"
                                            onClick={() => setIsDropdownOpen(false)}
                                        >
                                            <LogOut className="w-4 h-4 mr-2" />
                                            Sign out
                                        </button>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
            }
        </div>
    )
}

export default Header