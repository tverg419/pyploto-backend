import React from 'react';
import { Link } from 'react-router-dom'

function Nav(props) {
    return (
        <div>
            <Link to='/'>Home</Link>
            <Link to='/feed'>Feed</Link>
            <Link to='/login'>Login</Link>
            <Link to='/signup'>Sign-Up</Link>
        </div>
    );
}

export default Nav;