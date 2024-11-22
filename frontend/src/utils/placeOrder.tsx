import { getToken } from "./utils";

export const  orderInitiate = (event_id, quantity, price, offer_type)=>{
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const token = getToken()
    myHeaders.append("Authorization", "Bearer "+token);
    
    const raw = JSON.stringify({
      "event_id": event_id,
      "offer_type": offer_type,
      "order_type": "LO",
      "l1_order_quantity": quantity,
      "l1_expected_price": price
    });
    
    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
    };
    
    fetch("http://backend-service:8000/api/v1/oms/order/initiate", requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.error(error));
}