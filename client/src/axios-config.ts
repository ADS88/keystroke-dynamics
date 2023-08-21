import axios from "axios"

let baseURL = "http://localhost:5000"
const axiosInstance = axios.create({
  baseURL,
})

export default axiosInstance
