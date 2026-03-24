import { useState } from "react";
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function ReceptionistDashboard(){
    const [name, setName]=useState("")
    const [phone, setPhone]=useState("")

    const registerPatient=async()=>{
        await API.post('patients/register/', {
            full_name: name,
            phone:phone
        })
        alert('Patient Registered')
    }

    return(
        <DashboardLayout>
            <h1>Receptionist Dashboard</h1>

            <input
            placeholder="Patient Name"
            onChange={(e)=> setName(e.target.value)}/>

            <input
            placeholder="Phone"
            onChange={(e)=> setPhone(e.target.value)}/>
            <button onClick={registerPatient}>
                Register Patient
            </button>
        </DashboardLayout>
    )
}
export default ReceptionistDashboard