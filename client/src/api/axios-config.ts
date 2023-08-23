import axios from "axios"

let baseURL =
  process.env.NODE_ENV === "development"
    ? "http://localhost:80"
    : "keystroke-dynamics-server-lb-119970644.ap-southeast-2.elb.amazonaws.com"
const axiosInstance = axios.create({
  baseURL,
})

export default axiosInstance
