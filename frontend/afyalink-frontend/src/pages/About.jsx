import Navbar from "../components/Navbar"
import Footer from "../components/Footer"

function About() {

  return (

    <div>

      <Navbar />

      <div style={{
        padding: "100px",
        maxWidth: "900px",
        margin: "auto"
      }}>

        <h1>About AfyaLink</h1>

        <p style={{ marginTop: "20px" }}>

          AfyaLink is a health data integration platform designed
          to connect hospitals and patients across healthcare
          systems.

        </p>

        <p style={{ marginTop: "20px" }}>

          Our mission is to eliminate fragmented medical records
          and enable doctors to access patient history instantly,
          improving diagnosis accuracy and healthcare outcomes.

        </p>

        <h2 style={{ marginTop: "40px" }}>

          Founders

        </h2>

        <p style={{ marginTop: "20px" }}>

          AfyaLink was founded to address the challenge of
          disconnected hospital systems and empower patients
          with ownership of their medical data.

        </p>

      </div>

      <Footer />

    </div>

  )

}

export default About