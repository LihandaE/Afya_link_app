import { useEffect, useState } from "react"
import API from "../services/api"
import DashboardLayout from "../layouts/DashboardLayout"

function DoctorDashboard() {

  const [queue, setQueue] = useState([])

  useEffect(() => {

    loadQueue()

  }, [])

  const loadQueue = async () => {

    const res = await API.get('visits/doctor-queue/')

    setQueue(res.data)

  }

  return (

    <DashboardLayout>

      <h1>Doctor Queue</h1>

      {queue.map((visit) => (

        <div key={visit.id}>

          Patient Visit ID: {visit.id}

        </div>

      ))}

    </DashboardLayout>

  )
}

export default DoctorDashboard