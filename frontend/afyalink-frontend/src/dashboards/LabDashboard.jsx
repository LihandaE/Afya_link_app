import { useEffect, useState } from "react";
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout";

function LabDashboard(){
    const [tests, setTests]=useState([])
    useEffect(()=>{
        fetchLabQueue()
    }, [])
    const fetchLabQueue=async (id)=>{
        const result=prompt('Emter lab result')
        if (!result) return
        await API.post('lab/result/',{
            id:id,
            result:result
        })
        fetchLabQueue()
    }
    return (
        <DashboardLayout>
            <h1>Lab Dashboard</h1>
              {tests.map((test) => (
        <div key={test.id} style={card}>
          <p><b>Test:</b> {test.test_type}</p>
          <p><b>Visit:</b> {test.visit}</p>

          <button onClick={() => uploadResult(test.id)}>
            Upload Result
          </button>
        </div>
      ))}
        </DashboardLayout>
    )
}
export default LabDashboard

const card = {
  padding: "15px",
  margin: "10px 0",
  border: "1px solid #ddd"
}