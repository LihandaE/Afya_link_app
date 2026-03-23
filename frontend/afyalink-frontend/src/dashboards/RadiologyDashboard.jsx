import { useEffect, useState } from "react"
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function RadiologyDashboard() {

  const [scans, setScans] = useState([])

  useEffect(() => {
    fetchScans()
  }, [])

  const fetchScans = async () => {
    const res = await API.get("radiology/queue/")
    setScans(res.data)
  }

  const uploadResult = async (id) => {

    const result = prompt("Enter scan result")

    if (!result) return

    await API.post("radiology/result/", {
      id: id,
      result: result
    })

    fetchScans()
  }

  return (
    <DashboardLayout>

      <h1>Radiology Dashboard</h1>

      {scans.map((scan) => (
        <div key={scan.id} style={card}>
          <p><b>Scan:</b> {scan.scan_type}</p>

          <button onClick={() => uploadResult(scan.id)}>
            Upload Report
          </button>
        </div>
      ))}

    </DashboardLayout>
  )
}

export default RadiologyDashboard

const card = {
  padding: "15px",
  margin: "10px 0",
  border: "1px solid #ddd"
}