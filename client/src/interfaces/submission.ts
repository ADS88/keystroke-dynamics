import { KeyEvent } from "./keyevent"

export interface Submission {
  username: string
  sentenceId: number
  results: KeyEvent[]
}
