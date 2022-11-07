import { useEffect, useState } from "react";
import "./GasPrice.css"

const GasPrice = () => {
    const [gasPrice, setGasPrice] = useState({'low': {}, 'medium': {}, 'high': {}})

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:8000/api/gas_price')
            if (response.status === 200) {
                const gasPrice = await response.json();
                setGasPrice(gasPrice)
            } else {
                alert("an error occurred while getting gas estimation..")
            }
        })()
    }, [])

  return (
    <div className="GasPrice">
      <div className="row">
        <h1 style={{marginLeft: '25%'}}>Gas Estimation by Priority</h1>
        <div style={{backgroundColor: 'green'}} className="column">low: <label>{gasPrice.low.max_fee} gwei</label>
        <br></br>
        <div style={{fontSize: '11px'}}>
        Base: {gasPrice.low.adjusted_base_fee_in_gwei} | Priority: {gasPrice.low.max_priority_fee}
        </div>
        </div>
        <div style={{backgroundColor: 'blue'}} className="column">medium: <label>{gasPrice.medium.max_fee} gwei</label>
        <br></br>
        <div style={{fontSize: '11px'}}>
        Base: {gasPrice.medium.adjusted_base_fee_in_gwei} | Priority: {gasPrice.medium.max_priority_fee}
        </div>
        </div>
        <div style={{backgroundColor: 'red'}} className="column">high: <label>{gasPrice.high.max_fee} gwei</label>
        <br></br>
        <div style={{fontSize: '11px'}}>
        Base: {gasPrice.high.adjusted_base_fee_in_gwei} | Priority: {gasPrice.high.max_priority_fee}
        </div>
        </div>
        </div>
    </div>
  );
}

export default GasPrice;
