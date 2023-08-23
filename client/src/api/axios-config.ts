import axios from "axios"

let baseURL =
  import.meta.env.MODE === "development"
    ? "http://localhost:80"
    : "http://keystroke-dynamics-server-lb-119970644.ap-southeast-2.elb.amazonaws.com"
const axiosInstance = axios.create({
  baseURL,
})

export default axiosInstance
