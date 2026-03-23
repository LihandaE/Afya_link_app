import { useEffect, useState } from "react"
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function PharmacyDashboard() {

  const [prescriptions, setPrescriptions] = useState([])

  useEffect(() => {
    fetchQueue()
  }, [])

  const fetchQueue = async () => {
    const res = await API.get("pharmacy/queue/")
    setPrescriptions(res.data)
  }

  const dispense = async (id) => {

    await API.post("pharmacy/dispense/", {
      prescription: id
    })

    fetchQueue()
  }

  return (
    <DashboardLayout>

      <h1>Pharmacy Dashboard</h1>

      {prescriptions.map((p) => (
        <div key={p.id} style={card}>
          <p><b>Medication:</b> {p.medication}</p>

          <button onClick={() => dispense(p.id)}>
            Dispense
          </button>
        </div>
      ))}

    </DashboardLayout>
  )
}

export default PharmacyDashboard

const card = {
  padding: "15px",
  margin: "10px 0",
  border: "1px solid #ddd"
}