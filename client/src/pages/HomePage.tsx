import { useEffect, useState } from "react"
import SimilarTypists from "../components/SimilarTypists"
import { Submission } from "../interfaces"
import axiosInstance from "../axios-config"

const getSentence: () => Promise<{ text: string; id: number }> = async () => {
  const response = await axiosInstance.get("sentence")
  return response.data
}

const submitResults: () => Promise<string[]> = async () => {
  const submission: Submission = {
    results: [],
    username: "Test user",
    sentenceId: 1,
  }
  const response = await axiosInstance.post("/sentence", submission)
  return response.data
}

function HomePage() {
  const [sentence, setSentence] = useState("")
  const [sentenceId, setSentenceId] = useState(-1)

  const [name, setName] = useState("")
  const [similarTypistNames, setSimilarTypistNames] = useState<string[]>([])

  const handleNameChange = (event: any) => {
    setName(event.target.value)
  }

  const doneClicked = async () => {
    const response = await submitResults()
    setSimilarTypistNames(response)
  }

  const newSentence = () => {
    getSentence().then(sentence => {
      setSentence(sentence.text)
      setSentenceId(sentence.id)
    })
  }

  useEffect(() => newSentence(), [])

  const hasSubmitted = similarTypistNames.length > 0

  return (
    <>
      <main id="app" className="container">
        <h1>{sentence}</h1>
        <form>
          <label htmlFor="name">Name</label>
          <input type="text" id="name" name="fname" value={name} onChange={handleNameChange} />
          <label htmlFor="sentence-input">Sentence</label>
          <textarea id="sentence-input" name="sentence-input"></textarea>
        </form>
        {!hasSubmitted && <button onClick={doneClicked}>Done</button>}
        {hasSubmitted && <SimilarTypists names={similarTypistNames} />}
        {hasSubmitted && <button onClick={newSentence}>Try again</button>}
      </main>
    </>
  )
}

export default HomePage
