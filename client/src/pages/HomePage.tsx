import { useEffect, useState } from "react"
import SimilarTypists from "../components/SimilarTypists"
import { KeyEvent } from "../interfaces"
import { getSentence, submitResults } from "../api"

function HomePage() {
  const [sentence, setSentence] = useState({ id: -1, text: "" })
  const [username, setUsername] = useState("")

  const [similarTypistNames, setSimilarTypistNames] = useState<string[]>([])
  const [hasReceivedSimilarTypistNames, setHasReceivedSimilarTypistNames] = useState(false)

  const [keyEvents, setKeyEvents] = useState<KeyEvent[]>([])

  useEffect(() => newSentence(), [])

  const newSentence = () => {
    getSentence().then(sentence => {
      setSentence(sentence)
      setSimilarTypistNames([])
      setHasReceivedSimilarTypistNames(false)
      setKeyEvents([])
    })
  }

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value)
  }

  const handleDoneClicked = async () => {
    const similarTypists = await submitResults(username, sentence.id, keyEvents)
    setSimilarTypistNames(similarTypists)
    setHasReceivedSimilarTypistNames(true)
  }

  const handleSentenceKeyChange = ({ key, type, timeStamp }: React.KeyboardEvent<HTMLElement>) => {
    const newEvent: KeyEvent = { key, type, timestampMillis: timeStamp }
    setKeyEvents(previousEvents => [...previousEvents, newEvent])
  }

  return (
    <main className="container" style={{ marginTop: 60 }}>
      {!hasReceivedSimilarTypistNames && (
        <>
          <h1>{sentence.text}</h1>
          <form>
            <label htmlFor="name">Name</label>
            <input type="text" name="name" id="name" value={username} onChange={handleNameChange} />
            <label htmlFor="sentence">Sentence</label>
            <textarea
              id="sentence"
              name="sentence"
              onKeyDown={handleSentenceKeyChange}
              onKeyUp={handleSentenceKeyChange}
            ></textarea>
          </form>
          <button onClick={handleDoneClicked}>Done</button>
        </>
      )}
      {hasReceivedSimilarTypistNames && (
        <>
          <SimilarTypists names={similarTypistNames} />
          <button onClick={newSentence}>Go again!</button>
        </>
      )}
    </main>
  )
}

export default HomePage
