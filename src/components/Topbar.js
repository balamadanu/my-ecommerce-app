export default function Topbar() {
  return <header className="topbar">
    <button className="btn btn-light d-lg-none" aria-label="Menu"><i className="bi bi-list"></i></button>
    <div className="search-box"><i className="bi bi-search"></i><input placeholder="Search anything..." aria-label="Search" /></div>
    <div className="topbar-actions"><button className="icon-button" aria-label="Notifications"><i className="bi bi-bell"></i><span className="notification-dot"></span></button><div className="profile"><div className="avatar">AM</div><div className="d-none d-sm-block"><b>Admin Manager</b><small>Administrator</small></div><i className="bi bi-chevron-down small text-secondary"></i></div></div>
  </header>;
}