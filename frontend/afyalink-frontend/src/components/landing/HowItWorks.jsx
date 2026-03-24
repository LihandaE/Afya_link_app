function HowItWorks() {

  const steps = [

    "Patient registers at hospital",

    "Nurse records vitals",

    "Doctor performs diagnosis",

    "Lab and radiology tests conducted",

    "Pharmacist dispenses medication",

    "Records stored permanently on AfyaLink"

  ]

  return (

    <div style={{
      padding: "100px",
      background: "#f8fafc"
    }}>

      <h2 style={{
        textAlign: "center",
        fontSize: "36px"
      }}>

        How AfyaLink Works

      </h2>

      <div style={{
        marginTop: "60px",
        maxWidth: "600px",
        marginInline: "auto"
      }}>

        {steps.map((step, index) => (

          <div style={{
            display: "flex",
            gap: "20px",
            marginBottom: "20px"
          }}>

            <div style={{
              background: "#2563eb",
              color: "white",
              width: "30px",
              height: "30px",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              borderRadius: "50%"
            }}>

              {index + 1}

            </div>

            <p>{step}</p>

          </div>

        ))}

      </div>

    </div>

  )

}

export default HowItWorks