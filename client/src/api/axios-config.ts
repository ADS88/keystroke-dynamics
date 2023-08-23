import axios from "axios"

let baseURL =
  import.meta.env.MODE === "development"
    ? "http://localhost:80/api/v1"
    : "http://keystroke-dynamics-server-lb-119970644.ap-southeast-2.elb.amazonaws.com/api/v1"
const axiosInstance = axios.create({
  baseURL,
})

export default axiosInstance
