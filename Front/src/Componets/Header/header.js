import React from "react";
import './header.sass';
import Nav from '../nav/nav'

const Header = () => {
    return(
    <div className="container">
        <header className="header">
            <img src="image/logo.png" alt="" className="logo"> </img>
            <Nav />
            
        </header>
    </div>
    )
}
export default Header