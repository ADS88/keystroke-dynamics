import { useEffect, useState } from "react"
import SimilarTypists from "../components/SimilarTypists"
import { KeyEvent } from "../interfaces"
import { getSentence, submitResults } from "../api"
import SentenceInput from "../components/SentenceInput"

function HomePage() {
  const [sentence, setSentence] = useState({ id: -1, text: "" })
  const [username, setUsername] = useState("")

  const [similarTypistNames, setSimilarTypistNames] = useState<string[]>([])
  const [hasCompletedTest, setHasCompletedTest] = useState(false)

  const [keyEvents, setKeyEvents] = useState<KeyEvent[]>([])

  useEffect(() => newSentence(), [])

  const newSentence = () => {
    getSentence().then(sentence => {
      setSentence(sentence)
      setSimilarTypistNames([])
      setHasCompletedTest(false)
      setKeyEvents([])
    })
  }

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value)
  }

  const handleDoneClicked = async () => {
    const similarTypists = await submitResults(username, sentence.id, keyEvents)
    setSimilarTypistNames(similarTypists)
    setHasCompletedTest(true)
  }

  const handleSentenceKeyChange = ({ key, type, timeStamp }: React.KeyboardEvent<HTMLElement>) => {
    const newEvent: KeyEvent = { key, type, timestampMillis: timeStamp }
    setKeyEvents(previousEvents => [...previousEvents, newEvent])
  }

  return (
    <main className="container" style={{ marginTop: 60 }}>
      {hasCompletedTest ? (
        <SimilarTypists names={similarTypistNames} newSentence={newSentence} />
      ) : (
        <SentenceInput
          sentence={sentence.text}
          username={username}
          handleDoneClicked={handleDoneClicked}
          handleSentenceKeyChange={handleSentenceKeyChange}
          handleNameChange={handleNameChange}
        />
      )}
    </main>
  )
}

export default HomePage
