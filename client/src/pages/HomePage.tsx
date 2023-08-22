import { useEffect, useState, useRef } from "react"
import SimilarTypists from "../components/SimilarTypists"
import { KeyEvent } from "../interfaces"
import { getSentence, submitResults } from "../api"

function HomePage() {
  const [sentence, setSentence] = useState({ id: -1, text: "" })
  const [username, setUsername] = useState("")
  const [similarTypistNames, setSimilarTypistNames] = useState<string[]>([])
  const [keyEvents, setKeyEvents] = useState<KeyEvent[]>([])

  const sentenceInputReference = useRef<HTMLTextAreaElement>(null)
  const nameInputReference = useRef<HTMLInputElement>(null)

  useEffect(() => initialSentence(), [])

  const initialSentence = () => {
    getSentence().then(sentence => {
      setSentence(sentence)
      nameInputReference.current?.focus()
    })
  }

  const nextSentence = () => {
    getSentence().then(sentence => {
      setSentence(sentence)
      setSimilarTypistNames([])
      setTimeout(() => sentenceInputReference.current?.focus(), 100)
    })
  }

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value)
  }

  const handleDoneClicked = async () => {
    const similarTypists = await submitResults(username, sentence.id, keyEvents)
    setSimilarTypistNames(similarTypists)
  }

  const handleKeyChange = ({ key, type, timeStamp }: React.KeyboardEvent<HTMLElement>) => {
    const newEvent: KeyEvent = { key, type, timestampMillis: timeStamp }
    setKeyEvents(previousEvents => [...previousEvents, newEvent])
  }

  const hasSubmitted = similarTypistNames.length > 0

  return (
    <main className="container" style={{ marginTop: 60 }}>
      <h1>{sentence.text}</h1>
      {!hasSubmitted && (
        <>
          <form>
            <label htmlFor="name">Name</label>
            <input
              disabled={hasSubmitted}
              type="text"
              name="name"
              id="name"
              value={username}
              onChange={handleNameChange}
              ref={nameInputReference}
            />
            <label htmlFor="sentence-input">Sentence</label>
            <textarea
              ref={sentenceInputReference}
              disabled={hasSubmitted}
              id="sentence-input"
              name="sentence-input"
              onKeyDown={handleKeyChange}
              onKeyUp={handleKeyChange}
            ></textarea>
          </form>
          <button onClick={handleDoneClicked}>Done</button>
        </>
      )}
      {hasSubmitted && (
        <>
          <SimilarTypists names={similarTypistNames} />
          <button onClick={nextSentence}>Go again!</button>
        </>
      )}
    </main>
  )
}

export default HomePage
