interface SimilarTypistsProps {
  names: string[]
}

function SimilarTypists({ names }: SimilarTypistsProps) {
  const similarTypistNames = names.map(name => <li>{name}</li>)
  return (
    <>
      <h2>Your typing is most similar to</h2>
      <ol>{similarTypistNames}</ol>
    </>
  )
}

export default SimilarTypists
