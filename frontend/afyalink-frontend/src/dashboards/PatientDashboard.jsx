import { useState } from "react"
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"
import OTPModal from "../components/OTPModal"

function PatientDashboard() {

  const [history, setHistory] = useState(null)
  const [showModal, setShowModal] = useState(false)

  const patientId = 1

  const fetchHistory = async () => {

    try {

      const res = await API.get(`patients/history/${patientId}/`)
      setHistory(res.data)

    } catch (err) {

      if (err.response?.data?.error === "OTP verification required") {
        setShowModal(true)
      }

    }
  }

  return (

    <DashboardLayout>

      <h1>Patient Dashboard</h1>

      <button onClick={fetchHistory}>
        View Medical Records
      </button>

      {showModal && (
        <OTPModal
          patientId={patientId}
          onClose={() => setShowModal(false)}
          onSuccess={fetchHistory}
        />
      )}

      {history && (

        <div style={{ marginTop: "20px" }}>

          <h2>Medical History</h2>

          {history.visits.map((v) => (
            <div key={v.id} style={card}>
              Visit ID: {v.id}
            </div>
          ))}

        </div>

      )}

    </DashboardLayout>
  )
}

export default PatientDashboard

const card = {
  padding: "15px",
  border: "1px solid #ddd",
  marginTop: "10px"
}