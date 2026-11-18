const students = [
  ["Olivia Rhye","STU-2024-001","Grade 10 - A","olivia@example.com","Active","OR"],
  ["Phoenix Baker","STU-2024-014","Grade 9 - B","phoenix@example.com","Active","PB"],
  ["Lana Steiner","STU-2024-027","Grade 8 - A","lana@example.com","Pending","LS"],
  ["Demi Wilkinson","STU-2024-032","Grade 10 - C","demi@example.com","Active","DW"],
];
export default function StudentsTable() {
  return <section className="panel">
    <div className="panel-heading flex-wrap">
      <div>
        <h2 className="section-title">Recent Students</h2>
        <p className="small text-secondary mb-0">Recently enrolled students</p>
      </div>
    <div className="d-flex gap-2">
      <button className="btn btn-outline-secondary btn-sm">
        <i className="bi bi-funnel me-1"></i>Filter
      </button>
      <button className="btn btn-outline-secondary btn-sm">
        <i className="bi bi-download me-1"></i>Export
      </button>
    </div>
  </div>
    <div className="table-responsive">
      <table className="table align-middle student-table mb-0">
        <thead>
          <tr>
            <th>STUDENT</th>
            <th>STUDENT ID</th>
            <th>CLASS</th>
            <th>EMAIL</th>
            <th>STATUS</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {students.map(([name,id,grade,email,status,initials])=>
          <tr key={id}>
            <td>
              <div className="student-name">
                <span className="student-avatar">{initials}</span>
                <b>{name}</b>
              </div>
            </td>
            <td>{id}</td>
            <td>{grade}</td>
            <td>{email}</td>
            <td><span className={`status-pill ${status.toLowerCase()}`}>{status}</span></td>
            <td>
              <button className="btn btn-sm btn-light" aria-label={`More options for ${name}`}>
                <i className="bi bi-three-dots"></i>
              </button>
            </td>
          </tr>
        )}</tbody></table></div>
    <div className="table-bottom">
      <span>Showing 4 of 2,450 students</span>
      <div className="d-flex gap-2">
        <button className="btn btn-outline-secondary btn-sm" disabled>Previous</button>
        <button className="btn btn-outline-secondary btn-sm">Next</button>
      </div>
    </div>
  </section>;
}