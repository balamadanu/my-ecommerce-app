import Sidebar from './components/Sidebar.js'
import Topbar from './components/Topbar.js';
import StatCard from './components/StatCard.js';
import StudentsTable from './components/StudentsTable.js';

const stats = [
  { label: "Total Students", value: "2,450", change: "+12.5%", icon: "bi-people", tone: "purple" },
  { label: "Total Teachers", value: "148", change: "+4.2%", icon: "bi-person-workspace", tone: "blue" },
  { label: "Total Classes", value: "64", change: "+2.0%", icon: "bi-easel", tone: "orange" },
  { label: "Attendance Rate", value: "94.8%", change: "+1.8%", icon: "bi-calendar-check", tone: "green" },
];

function App() {
  return (
   <div className="app-shell">
      <Sidebar />
      <main className="main-content">
        <Topbar />
        <div className="container-fluid dashboard-content">
          <div className="d-flex flex-wrap justify-content-between align-items-center gap-3 mb-4">
            <div>
              <p className="eyebrow mb-1">OVERVIEW</p>
              <h1 className="page-title mb-1">School Dashboard</h1>
              <p className="text-secondary mb-0">Welcome back! Here's what's happening at your school today.</p>
            </div>
            <button className="btn btn-primary px-3"><i className="bi bi-plus-lg me-2"></i>Add New Student</button>
          </div>

          <div className="row g-3 mb-4">
            {stats.map((stat) => <div className="col-12 col-sm-6 col-xl-3" key={stat.label}><StatCard {...stat} /></div>)}
          </div>

          <div className="row g-3 mb-4">
            <div className="col-12 col-xl-8">
              <section className="panel h-100">
                <div className="panel-heading">
                  <div><h2 className="section-title">Attendance Overview</h2><p className="small text-secondary mb-0">Weekly student attendance</p></div>
                  <select className="form-select form-select-sm filter-select" aria-label="Select period"><option>This Week</option><option>This Month</option></select>
                </div>
                <div className="attendance-chart">
                  {[62, 78, 70, 91, 84, 96, 73].map((height, i) => <div className="chart-column" key={i}><div className="chart-track"><div className={`chart-bar ${i === 5 ? "highlight" : ""}`} style={{height: `${height}%`}}></div></div><span>{["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][i]}</span></div>)}
                </div>
                <div className="chart-legend"><span><i className="legend-dot"></i>Present students</span><strong>94.8% <small className="text-success fw-normal">+2.4%</small></strong></div>
              </section>
            </div>
            <div className="col-12 col-xl-4">
              <section className="panel h-100">
                <div className="panel-heading"><div><h2 className="section-title">Upcoming Events</h2><p className="small text-secondary mb-0">School calendar</p></div><button className="btn btn-link btn-sm text-decoration-none">View all</button></div>
                <div className="event-item"><div className="date-tile"><b>22</b><span>JUN</span></div><div><b>Parent-Teacher Meeting</b><p className="small text-secondary mb-0">09:00 AM · Main Hall</p></div></div>
                <div className="event-item"><div className="date-tile date-blue"><b>25</b><span>JUN</span></div><div><b>Science Exhibition</b><p className="small text-secondary mb-0">10:30 AM · Science Block</p></div></div>
                <div className="event-item"><div className="date-tile date-orange"><b>28</b><span>JUN</span></div><div><b>Sports Day</b><p className="small text-secondary mb-0">08:00 AM · School Ground</p></div></div>
              </section>
            </div>
          </div>

          <StudentsTable />
          <footer className="dashboard-footer">© 2026 EduAdmin School Management · Dashboard template</footer>
        </div>
      </main>
    </div>
  );
}

export default App;
