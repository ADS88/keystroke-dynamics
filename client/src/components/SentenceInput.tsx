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

  const submitDisabled = !username.trim() || !typedSentence.trim()

  return (
    <>
      <h1>{sentence}</h1>
      <label htmlFor="sentence">Type the text passage into the box below</label>
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
        <label htmlFor="name">Then type your name in this box</label>
        <input type="text" name="name" id="name" value={username} onChange={handleNameChange} />
      </form>
      <button onClick={handleDoneClicked} disabled={submitDisabled}>
        Done
      </button>
    </>
  )
}

export default SentenceInput
