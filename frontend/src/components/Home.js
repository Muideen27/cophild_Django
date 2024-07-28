import React from 'react';
import './Home.css';
import logo from '../assets/logo.jpeg'; // Adjust the path according to your folder structure

const Home = () => {
  return (
    <div className="home">
      <header className="header">
        <img src={logo} alt="Logo" className="logo" />
        <nav>
          <ul className="nav-list">
            <li>Learning</li>
            <li>Community</li>
            <li>Job Opportunities</li>
            <li>Professional Profile</li>
            <li>Sailors Points</li>
            <li>Contact us</li>
          </ul>
        </nav>
        <button className="join-button">Join Our Community</button>
      </header>
      <div className="content">
        <h1>Welcome to the Alumni Website</h1>
        <p>This is where you can find information and resources for alumni.</p>
      </div>
    </div>
  );
};

export default Home;
