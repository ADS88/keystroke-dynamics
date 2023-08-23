interface SimilarTypistsProps {
  names: string[]
  newSentence: () => void
}

function SimilarTypists({ names, newSentence }: SimilarTypistsProps) {
  const similarTypistNames = names.map(name => <li key={name}>{name}</li>)

  const headingText =
    names.length > 0
      ? "Your typing is most similar to:"
      : "No similar people could be found. You are likely the first person using this app! Come back soon, or try again under a different name."

  return (
    <>
      <h2 data-testid="similar-names-heading">{headingText}</h2>
      <ol data-testid="similar-names-list">{similarTypistNames}</ol>
      <button onClick={newSentence}>Go again!</button>
    </>
  )
}

export default SimilarTypists
