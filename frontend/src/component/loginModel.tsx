// App.js
import { Dialog } from '@headlessui/react';
import { useState, useRef, useEffect} from 'react';
import { AiOutlineClose } from 'react-icons/ai';
import { toast, Bounce } from 'react-toastify';

const getUserBalance = (token, setUserBalance) => {
    const myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${token}`);

    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };

    fetch("http://backend.ansarisaif.com/api/v1/user/balance", requestOptions)
        .then((response) => {
            if (response.status == 200) {
                return response.json()
            } else {
                return false;
            }
        })
        .then((result) => {
            if (result) {
                setUserBalance(Number(result.balance))
            }
        })
        .catch((error) => console.error(error));
}

function loginModel({ isOpen, setIsOpen, setUserBalance }) {
    const [firstStep, setFirstStep] = useState(true)
    const [phoneNumber, setPhoneNumber] = useState('');
    const inputRef = useRef(null);

    const [otp1, setOtp1] = useState("");
    const [otp2, setOtp2] = useState("");
    const [otp3, setOtp3] = useState("");
    const [otp4, setOtp4] = useState("");
    const [otp5, setOtp5] = useState("");
    const [otp6, setOtp6] = useState("");

    const clearOtp = () => {
        setOtp1("");
        setOtp2("");
        setOtp3("");
        setOtp4("");
        setOtp5("");
        setOtp6("");
        setFirstStep(true);
        setPhoneNumber("")
    }
    useEffect(() => {
        if (!firstStep){
            inputRef.current.focus();
        }
    }, [firstStep])
    
    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPhoneNumber(e.target.value);
    };
    const handleOtpChange = (e: React.ChangeEvent<HTMLInputElement>, func) => {
        func(e.target.value);
    };

    const handleSubmit = () => {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const raw = JSON.stringify({
            "mobile": phoneNumber
        });

        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };

        fetch("http://backend.ansarisaif.com/api/v1/user/login", requestOptions)
            .then((response) => {
                if (response.status === 200) {
                    setFirstStep(false);
                    toast('✅ Please check SMS section for the OTP!!', {
                        position: "top-center",
                        autoClose: 2500,
                        hideProgressBar: false,
                        closeOnClick: false,
                        pauseOnHover: false,
                        draggable: true,
                        progress: undefined,
                        theme: "light",
                        transition: Bounce,
                    });

                } else {
                    toast('ⓧ Something went wrong!!', {
                        position: "top-center",
                        autoClose: 2500,
                        hideProgressBar: false,
                        closeOnClick: false,
                        pauseOnHover: false,
                        draggable: true,
                        progress: undefined,
                        theme: "light",
                        transition: Bounce,
                    });
                }
                return response.json()
            }
            )
            .then((result) => {
                // success logic here
            })
            .catch((error) => console.error(error));
    };

    const handleSubmitVerifyOtp = () => {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        const otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6;
        const raw = JSON.stringify({
            "mobile": phoneNumber,
            "otp": otp
        });

        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };

        fetch("http://backend.ansarisaif.com/api/v1/user/validateOtp", requestOptions)
            .then((response) => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    return false
                }

            })
            .then((result) => {
                if (result) {
                    setIsOpen(false);
                    localStorage.access_token = result.access_token
                    getUserBalance(result.access_token, setUserBalance)
                    toast('✅ Logged in successfully', {
                        position: "top-center",
                        autoClose: 2500,
                        hideProgressBar: false,
                        closeOnClick: false,
                        pauseOnHover: false,
                        draggable: true,
                        progress: undefined,
                        theme: "light",
                        transition: Bounce,
                    });
                    
                    clearOtp();

                } else {
                    toast('ⓧ Invalid OTP', {
                        position: "top-center",
                        autoClose: 2500,
                        hideProgressBar: false,
                        closeOnClick: false,
                        pauseOnHover: false,
                        draggable: true,
                        progress: undefined,
                        theme: "light",
                        transition: Bounce,
                    });
                }
            })
            .catch((error) => console.error("error - code phat gya "));
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
                    {
                        firstStep ?
                            <>
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
                                    className={`w-full py-2 rounded-md text-white ${phoneNumber ? 'bg-blue-500 hover:bg-blue-600' : 'bg-gray-300'}`}
                                >
                                    Get OTP
                                </button>
                            </> :
                            <>
                                <div className="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
                                    <div className="bg-white rounded-lg shadow-lg w-full max-w-md p-6">
                                        <h2 className="text-xl font-semibold text-gray-800 mb-2">Verify phone</h2>
                                        <p className="text-gray-600 mb-4">OTP has been sent to +91-{phoneNumber}</p>

                                        <div className="flex justify-center gap-2 mb-4">
                                            <input
                                                ref={inputRef}
                                                type="text"
                                                maxLength={1}
                                                value={otp1}
                                                onChange={(e) => handleOtpChange(e, setOtp1)}
                                                onKeyUp={(e) => {
                                                    if (e.key !== "Backspace" && e.target.value) {
                                                        document.querySelector('input[name="otp2"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp1"
                                            />
                                            <input
                                                type="text"
                                                maxLength={1}
                                                value={otp2}
                                                onChange={(e) => handleOtpChange(e, setOtp2)}
                                                onKeyUp={(e) => {
                                                    if (e.key === "Backspace" && !e.target.value) {
                                                        document.querySelector('input[name="otp1"]')?.focus();
                                                    } else if (e.key !== "Backspace" && e.target.value) {
                                                        document.querySelector('input[name="otp3"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp2"
                                            />
                                            <input
                                                type="text"
                                                maxLength={1}
                                                value={otp3}
                                                onChange={(e) => handleOtpChange(e, setOtp3)}
                                                onKeyUp={(e) => {
                                                    if (e.key === "Backspace" && !e.target.value) {
                                                        document.querySelector('input[name="otp2"]')?.focus();
                                                    } else if (e.key !== "Backspace" && e.target.value) {
                                                        document.querySelector('input[name="otp4"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp3"
                                            />
                                            <input
                                                type="text"
                                                maxLength={1}
                                                value={otp4}
                                                onChange={(e) => handleOtpChange(e, setOtp4)}
                                                onKeyUp={(e) => {
                                                    if (e.key === "Backspace" && !e.target.value) {
                                                        document.querySelector('input[name="otp3"]')?.focus();
                                                    } else if (e.key !== "Backspace" && e.target.value) {
                                                        document.querySelector('input[name="otp5"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp4"
                                            />
                                            <input
                                                type="text"
                                                maxLength={1}
                                                value={otp5}
                                                onChange={(e) => handleOtpChange(e, setOtp5)}
                                                onKeyUp={(e) => {
                                                    if (e.key === "Backspace" && !e.target.value) {
                                                        document.querySelector('input[name="otp4"]')?.focus();
                                                    } else if (e.key !== "Backspace" && e.target.value) {
                                                        document.querySelector('input[name="otp6"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp5"
                                            />
                                            <input
                                                type="text"
                                                maxLength={1}
                                                value={otp6}
                                                onChange={(e) => handleOtpChange(e, setOtp6)}
                                                onKeyUp={(e) => {
                                                    if (e.key === "Backspace" && !e.target.value) {
                                                        document.querySelector('input[name="otp5"]')?.focus();
                                                    }
                                                }}
                                                className="w-10 h-10 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                name="otp6"
                                            />
                                        </div>
                                        <button
                                            onClick={handleSubmitVerifyOtp}
                                            className={`w-full py-2 rounded-md text-white bg-blue-500 hover:bg-blue-600`}
                                        >
                                            Verify
                                        </button>
                                    </div>
                                </div>

                            </>
                    }
                </div>
            </div>
        </Dialog>
    );
}

export default loginModel;
