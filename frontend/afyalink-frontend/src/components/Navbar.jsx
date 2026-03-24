import {Link} from "react-router-dom"
function Navbar(){
    return(
        <div style={{
            display: 'flex',
            justifyContent:'space-between',
            padding:'20px 60px',
            background: '#ffffff',
            borderBottom:'1px solid #eee'
            
        }}>
            <h2 style={{color:'#2563eb'}}>AfyaLink</h2>
            <div style={{display: 'flex', gap: '30px'}}>
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
                <Link to="/login">Login</Link>
            </div>
        </div>
    )
}
export default Navbar