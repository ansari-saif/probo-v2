// App.js
import { Dialog } from '@headlessui/react';
import { useState } from 'react';
import { AiOutlineClose } from 'react-icons/ai';

function loginModel({ isOpen, setIsOpen }) {

    const [phoneNumber, setPhoneNumber] = useState('');

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPhoneNumber(e.target.value);
    };

    const handleSubmit = () => {
        // Handle OTP request submission here
        console.log('Requesting OTP for:', phoneNumber);
    };
    return (
        <Dialog open={isOpen} onClose={() => setIsOpen(false)} className="fixed inset-0 z-10 flex items-center justify-center">
            <div className="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
                <div className="bg-white rounded-lg shadow-lg w-full max-w-md p-6">
                    <div className="flex justify-end">
                        <button onClick={() => setIsOpen(false)} className="text-gray-500 hover:text-gray-700">
                            <AiOutlineClose className="h-6 w-6" />
                        </button>
                    </div>
                    <h2 className="text-2xl font-semibold text-gray-800 mb-4">Enter your mobile number</h2>
                    <p className="text-gray-600 mb-4">We’ll send you an OTP</p>
                    <div className="flex items-center mb-4 border rounded-md overflow-hidden">
                        <span className="bg-gray-200 px-3 py-2 text-gray-800">+91</span>
                        <input
                            type="text"
                            placeholder="Phone number"
                            value={phoneNumber}
                            onChange={handleInputChange}
                            className="w-full p-2 focus:outline-none"
                        />
                    </div>
                    <p className="text-xs text-gray-500 mb-4">
                        By continuing, you accept that you are 18+ years of age & agree to the{' '}
                        <a href="#" className="text-blue-500 hover:underline">
                            Terms and Conditions
                        </a>
                        .
                    </p>
                    <button
                        onClick={handleSubmit}
                        disabled={!phoneNumber}
                        className={`w-full py-2 rounded-md text-white ${phoneNumber ? 'bg-blue-500 hover:bg-blue-600' : 'bg-gray-300'
                            }`}
                    >
                        Get OTP
                    </button>
                </div>
            </div>
        </Dialog>
    );
}

export default loginModel;
