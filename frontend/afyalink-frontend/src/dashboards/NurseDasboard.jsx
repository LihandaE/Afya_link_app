import { useEffect, useState } from "react";
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function NurseDashboard(){
    const [patients, setPatients]=useState([])
    useEffect(() => {
        fetchQueue()
    }, [])
    const fetchQeue=async ()=>{
        const res=await API.get('visits/nurse-queue')
        setPatients(res.data)

    }
    return (
        <DashboardLayout>
            <h1>Nurse Queue</h1>
            {patients.map((visit)=>(
                <div key={visit.id}>
                    {visit.patient}
                </div>
            ))}
        </DashboardLayout>
    )
}
export default NurseDashboard