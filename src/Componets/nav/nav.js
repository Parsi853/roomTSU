import React from "react";
import { Link } from "react-router-dom";
import'./nav.sass'

const Nav = () =>{
    return(
        <nav className="menu">
            <Link to='/'>Главная</Link>
            <Link to='/****'>Главная</Link>
            <Link to='/****'>Главная</Link>
            <Link to='/****'>Главная</Link>
        </nav>
    )

}
export default Nav