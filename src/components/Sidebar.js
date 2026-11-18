const links = [
  ["grid-1x2", "Dashboard", true],
  ["people", "Students"],
  ["person-workspace", "Teachers"],
  ["mortarboard", "Classes"],
  ["calendar-check", "Attendance"],
  ["journal-bookmark", "Examinations"],
  ["cash-coin", "Fees & Payments"],
  ["calendar-event", "Timetable"],
  ["bar-chart", "Reports"],
];
export default function Sidebar() {
  return <aside className="sidebar">
    <a className="brand" href="#"><span className="brand-mark"><i className="bi bi-mortarboard-fill"></i></span><span>Edu<span>Admin</span></span></a>
    <div className="sidebar-label">MENU</div>
    <nav className="nav flex-column">{links.map(([icon, label, active]) => <a href="#" key={label} className={`nav-link ${active ? "active" : ""}`}><i className={`bi bi-${icon}`}></i>{label}</a>)}</nav>
    <div className="sidebar-bottom"><div className="help-card"><i className="bi bi-headset"></i><b>Need help?</b><p>Contact our support team</p><button className="btn btn-sm btn-light w-100">Get Support</button></div><a href="#" className="nav-link"><i className="bi bi-gear"></i>Settings</a></div>
  </aside>;
}