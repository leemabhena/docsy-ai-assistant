import React from "react";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h1 className="sidebar__heading">Past Conversations</h1>
      <div className="conversation__wrapper">
        <p className="conversation_date">Today</p>
        <ul className="sidebar__list">
          <li className="sidebar__item">Patient John Doe</li>
          <li className="sidebar__item">Patient Jane Smith</li>
          <li className="sidebar__item">Patient Mike Johnson</li>
          <li className="sidebar__item">Patient Jane Doe</li>
        </ul>
      </div>
      <div className="conversation__wrapper">
        <p className="conversation_date">Yesterday</p>
        <ul className="sidebar__list">
          <li className="sidebar__item">Patient John Doe</li>
          <li className="sidebar__item">Patient Jane Smith</li>
          <li className="sidebar__item">Patient Mike Johnson</li>
        </ul>
      </div>
      <div className="conversation__wrapper">
        <p className="conversation_date">Past Week</p>
        <ul className="sidebar__list">
          <li className="sidebar__item">Patient John Doe</li>
          <li className="sidebar__item">Patient Jane Smith</li>
          <li className="sidebar__item">Patient Mike Johnson</li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
