import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { EventDetailsPage } from "./eventDetailsPage";
import { LandingPage } from "./landingPage";
import { EventPage } from "./eventPage";
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import Header from "./component/header";

function App() {
  return (
    <>
      <Router>
        <div className="bg-[#F5F5F5] w-full h-full">
        <ToastContainer />
        <Header/>


          {/* <Watchlist /> */}
          <Routes>
            <Route path="/" element={<LandingPage/>} />
            <Route path="/events" element={<EventPage />} />
            <Route path="/event-details" element={<EventDetailsPage />} />
          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
