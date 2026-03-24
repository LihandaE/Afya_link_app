function Hero(){
    return(
      <div style={{
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      padding: "100px",
      background: "#f8fafc"
    }}>
        <div>
            <h1 style={{
                fontSize:'48px',
                maxWidth:'500px'
            }}>
            Unified Healthcare Data Across Hospitals

            </h1>
       <p style={{
        marginTop:'20px',
        fontSize:'18px',
        color:'#555'
       }}>
        AfyaLink connects hospitals and patients through a secure 
        health data network, enabling doctors to access patient
        history instantly and improve healthcare outcomes.
        </p> 
        <button style={{
            marginTop: '30px',
            padding: '14px 30px',
            background: '#2563eb',
            color:'white',
            border: 'none',
            borderRadius: '8px'
        }}>
            Get Started

        </button>
          <img
        src="https://cdn.dribbble.com/userupload/7215424/file/original-7d28d414e644e2bc66426740d86ec353.png"
        width="500"
      />
        </div>

      </div>  
    )
}

export default Hero