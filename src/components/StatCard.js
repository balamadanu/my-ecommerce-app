export default function StatCard({ label, value, change, icon, tone }) {
  return <section className="stat-card">
    <div className="d-flex justify-content-between align-items-start">
      <div>
        <p className="stat-label">{label}</p>
        <h2 className="stat-value">{value}</h2>
     </div>
        <div className={`stat-icon ${tone}`}>
          <i className={`bi ${icon}`}></i>
        </div>
    </div>
          <p className="stat-change mb-0">
            <i className="bi bi-arrow-up-right"></i> {change} <span>from last month</span>
         </p>
    </section>;
}