import { useState } from "react"
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function AdminDashboard() {

  const [name, setName] = useState("")
  const [role, setRole] = useState("")
  const [email, setEmail] = useState("")

  const addStaff = async () => {

    await API.post("staff/add/", {
      full_name: name,
      role: role,
      email: email
    })

    alert("Staff added")
  }

  return (
    <DashboardLayout>

      <h1>Hospital Admin Dashboard</h1>

      <input placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />

      <select onChange={(e) => setRole(e.target.value)}>
        <option value="">Select Role</option>
        <option value="doctor">Doctor</option>
        <option value="nurse">Nurse</option>
        <option value="lab_tech">Lab Tech</option>
        <option value="pharmacist">Pharmacist</option>
        <option value="radiologist">Radiologist</option>
        
      </select>

      <button onClick={addStaff}>
        Add Staff
      </button>

    </DashboardLayout>
  )
}

export default AdminDashboard