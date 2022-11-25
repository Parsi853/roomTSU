import React from "react";
import{Route, Routes} from"react-router-dom";
import Header from "./Componets/Header/header";
import Page from "./pages/page";

function App() {
  return (
    <div className="wrapper">

    <Header/>
      <Routes>
        <Route path="/" element={<Page img='image/bg.jpg' title='Лунатики'/>}/>
        <Route path="/***" element={<Page img='image/bg.jpg' title='Лунатики'/>}/>
        <Route path="/***" element={<Page img='image/bg.jpg' title='Лунатики'/>}/>
        <Route path="/***" element={<Page img='image/bg.jpg' title='Лунатики'/>}/>


      </Routes>
    <Page img='image/bg.jpg' title="Лунатики" />
    </div>
  );
}

export default App;
