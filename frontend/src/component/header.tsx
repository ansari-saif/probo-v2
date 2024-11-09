import { useState } from "react";
import LoginModel from "./loginModel"

const checkIsLoggedIn = () => {
    console.log(localStorage.access_token);
    
    return localStorage.access_token
}
const Header = () => {
    const [isOpen, setIsOpen] = useState(false);


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
                    <>
                        <h1>Logged in</h1>
                    </>
            }
        </div>
    )
}

export default Header