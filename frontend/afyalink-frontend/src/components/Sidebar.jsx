import {Link} from "react-router-dom"

function Sidebar(){
    return (
        <div style={{
            width: "220px",
            height: "100vh",
            background: "#111827",
            color: "white",
            padding: "20px"
        }}>
            <h2>AfyaLink</h2>
            <ul style={{listStyle:"none", padding:0}}>
                <li>
          <Link to="/dashboard">Dashboard</Link>
        </li>

        <li>
          <Link to="/patients">Patients</Link>
        </li>

        <li>
          <Link to="/reports">Reports</Link>
        </li>

        <li>
          <Link to="/settings">Settings</Link>
        </li>
            </ul>
        </div>
    )
}

export default Sidebar