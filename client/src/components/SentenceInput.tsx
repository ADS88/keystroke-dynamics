import { useEffect, useRef, useState } from "react"

interface SentenceInputProps {
  sentence: string
  username: string
  handleDoneClicked: () => Promise<void>
  handleSentenceKeyChange: (event: React.KeyboardEvent<HTMLElement>) => void
  handleNameChange: (event: React.ChangeEvent<HTMLInputElement>) => void
}

function SentenceInput({
  sentence,
  username,
  handleDoneClicked,
  handleSentenceKeyChange,
  handleNameChange,
}: SentenceInputProps) {
  const sentenceInputRef = useRef<HTMLTextAreaElement>(null)
  const [typedSentence, setTypedSentence] = useState("")
  useEffect(() => sentenceInputRef.current?.focus(), [])

  const handleTypedSentenceChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setTypedSentence(event.target.value)
  }

  const submitDisabled = username.length === 0 || typedSentence.length === 0

  return (
    <>
      <h1>{sentence}</h1>
      <label htmlFor="sentence">Sentence</label>
      <textarea
        id="sentence"
        name="sentence"
        onKeyDown={handleSentenceKeyChange}
        onKeyUp={handleSentenceKeyChange}
        ref={sentenceInputRef}
        value={typedSentence}
        onChange={handleTypedSentenceChange}
      ></textarea>
      <form>
        <label htmlFor="name">Name</label>
        <input type="text" name="name" id="name" value={username} onChange={handleNameChange} />
      </form>
      <button onClick={handleDoneClicked} disabled={submitDisabled}>
        Done
      </button>
    </>
  )
}

export default SentenceInput
