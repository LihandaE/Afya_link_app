function Features() {

  const features = [

    {
      title: "Centralized Patient Records",
      text: "Patients can access their medical history from any hospital connected to AfyaLink."
    },

    {
      title: "Hospital Integration",
      text: "Hospitals share patient records securely while maintaining strict privacy control."
    },

    {
      title: "Real-Time Workflow",
      text: "Doctors, nurses, and pharmacists collaborate seamlessly within one system."
    },

    {
      title: "Secure Access",
      text: "Patient records require OTP authorization before viewing across hospitals."
    }

  ]

  return (

    <div style={{
      padding: "100px",
      background: "white"
    }}>

      <h2 style={{ textAlign: "center", fontSize: "36px" }}>

        Platform Features

      </h2>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(4,1fr)",
        gap: "40px",
        marginTop: "60px"
      }}>

        {features.map((f) => (

          <div style={{
            padding: "30px",
            background: "#f9fafb",
            borderRadius: "12px"
          }}>

            <h3>{f.title}</h3>

            <p>{f.text}</p>

          </div>

        ))}

      </div>

    </div>

  )

}

export default Features