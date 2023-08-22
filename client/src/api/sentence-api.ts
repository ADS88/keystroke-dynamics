import axiosInstance from "./axios-config"
import { KeyEvent, Submission } from "../interfaces"

export const getSentence = async () => {
  const response = await axiosInstance.get<{ id: number; text: string }>("/sentence")
  return response.data
}

export const submitResults = async (username: string, sentenceId: number, results: KeyEvent[]) => {
  const submission: Submission = { username, sentenceId, results }
  const response = await axiosInstance.post<string[]>("/sentence", submission)
  return response.data
}
