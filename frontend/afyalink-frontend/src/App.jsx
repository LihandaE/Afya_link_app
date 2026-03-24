import { BrowserRouter, Routes, Route } from "react-router-dom"
import ProtectedRoute from "./components/ProtectedRoute"

// Pages
import Home from "./pages/Home"
import About from "./pages/About"
import Login from "./pages/Login"

// Dashboards
import ReceptionistDashboard from "./dashboards/ReceptionistDashboard"
import NurseDashboard from "./dashboards/NurseDashboard"
import DoctorDashboard from "./dashboards/DoctorDashboard"
import LabDashboard from "./dashboards/LabDashboard"
import RadiologyDashboard from "./dashboards/RadiologyDashboard"
import PharmacyDashboard from "./dashboards/PharmacyDashboard"
import AdminDashboard from "./dashboards/AdminDashboard"
import PatientDashboard from "./dashboards/PatientDashboard"

function App() {

  return (

    <BrowserRouter>

      <Routes>

        {/* Public */}
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />

        {/* Protected Routes */}
        <Route path="/receptionist" element={
          <ProtectedRoute><ReceptionistDashboard /></ProtectedRoute>
        } />

        <Route path="/nurse" element={
          <ProtectedRoute><NurseDashboard /></ProtectedRoute>
        } />

        <Route path="/doctor" element={
          <ProtectedRoute><DoctorDashboard /></ProtectedRoute>
        } />

        <Route path="/lab" element={
          <ProtectedRoute><LabDashboard /></ProtectedRoute>
        } />

        <Route path="/radiology" element={
          <ProtectedRoute><RadiologyDashboard /></ProtectedRoute>
        } />

        <Route path="/pharmacy" element={
          <ProtectedRoute><PharmacyDashboard /></ProtectedRoute>
        } />

        <Route path="/admin" element={
          <ProtectedRoute><AdminDashboard /></ProtectedRoute>
        } />

        <Route path="/patient" element={
          <ProtectedRoute><PatientDashboard /></ProtectedRoute>
        } />

      </Routes>

    </BrowserRouter>

  )
}

export default App