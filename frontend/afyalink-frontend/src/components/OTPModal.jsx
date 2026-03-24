import { useState } from "react"
import API from "../services/api"

function OTPModal({ patientId, onClose, onSuccess }) {

  const [otp, setOtp] = useState("")
  const [loading, setLoading] = useState(false)

  const requestOTP = async () => {

    setLoading(true)

    try {
      await API.post("otp/send/", { patient_id: patientId })
      alert("OTP sent")
    } catch (err) {
      alert("Error sending OTP")
    }

    setLoading(false)
  }

  const verifyOTP = async () => {

    setLoading(true)

    try {

      await API.post("otp/verify/", {
        patient_id: patientId,
        otp: otp
      })

      alert("OTP verified")

      onSuccess()
      onClose()

    } catch (err) {
      alert("Invalid OTP")
    }

    setLoading(false)
  }

  return (

    <div style={overlay}>

      <div style={modal}>

        <h3>OTP Verification</h3>

        <button onClick={requestOTP}>
          Request OTP
        </button>

        <input
          placeholder="Enter OTP"
          value={otp}
          onChange={(e) => setOtp(e.target.value)}
        />

        <button onClick={verifyOTP}>
          Verify
        </button>

        <button onClick={onClose}>
          Cancel
        </button>

      </div>

    </div>
  )
}

export default OTPModal

const overlay = {
  position: "fixed",
  top: 0,
  left: 0,
  width: "100%",
  height: "100%",
  background: "rgba(0,0,0,0.5)",
  display: "flex",
  justifyContent: "center",
  alignItems: "center"
}

const modal = {
  background: "white",
  padding: "30px",
  borderRadius: "10px",
  width: "300px",
  display: "flex",
  flexDirection: "column",
  gap: "10px"
}