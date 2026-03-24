import { useState, useContext } from "react"
import { useNavigate } from "react-router-dom"
import API from "../services/api"
import { AuthContext } from "../context/AuthContext"

function Login() {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const { login } = useContext(AuthContext)
  const navigate = useNavigate()

  const handleLogin = async () => {

    try {

      const res = await API.post("auth/login/", {
        email,
        password
      })

      login(res.data)

      const role = res.data.user.role

      // =========================
      // ROLE-BASED REDIRECTION
      // =========================

      if (role === "receptionist") navigate("/receptionist")
      else if (role === "nurse") navigate("/nurse")
      else if (role === "doctor") navigate("/doctor")
      else if (role === "lab_tech") navigate("/lab")
      else if (role === "radiologist") navigate("/radiology")
      else if (role === "pharmacist") navigate("/pharmacy")
      else if (role === "hospital_admin") navigate("/admin")
      else if (role === "patient") navigate("/patient")

    } catch (err) {
      alert("Invalid credentials")
    }
  }

  return (

    <div style={container}>

      <div style={card}>

        <h2>AfyaLink Login</h2>

        <input
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={handleLogin}>
          Login
        </button>

      </div>

    </div>

  )
}

export default Login


const container = {
  height: "100vh",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  background: "#f3f4f6"
}

const card = {
  background: "white",
  padding: "40px",
  borderRadius: "10px",
  display: "flex",
  flexDirection: "column",
  gap: "15px",
  width: "300px"
}