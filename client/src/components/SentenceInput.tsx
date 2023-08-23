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
  return (
    <>
      <h1>{sentence}</h1>
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
  )
}

export default SentenceInput
