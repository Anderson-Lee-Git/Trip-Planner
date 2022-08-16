import { Routes, Route} from "react-router-dom";

import Home from "./Pages/Home"
import TransactionSheet from "./Pages/TransactionSheet";
import Trip from "./Pages/Trip";
import {sample_package_data} from "./DummyInfo/sample_package_data"

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home/>}/> 
        <Route path="/currenttrip" element={<Trip title={0}/>}/>
        <Route path="/transactionsheet" element={<TransactionSheet transaction={0}/>}/>
      </Routes>
    </div>
  );
}

export default App;
