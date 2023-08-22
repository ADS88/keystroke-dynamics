import { render, screen } from "@testing-library/react"
import SimilarTypists from "./SimilarTypists"

it("Test shows the users an informative message if no similar names are found", () => {
  render(<SimilarTypists names={[]} />)

  const heading = screen.getByTestId("similar-names-heading")
  expect(heading).toContainHTML("No similar people could be found")

  const similarTypistNames = screen.getByTestId("similar-names-list")
  const childNodes = similarTypistNames?.childNodes
  expect(childNodes?.length).toEqual(0)
})

it("Renders the similar typists names", () => {
  render(<SimilarTypists names={["Andrew", "Frankie", "Fletcher"]} />)

  const heading = screen.getByTestId("similar-names-heading")
  expect(heading).toContainHTML("most similar to")

  const similarTypistNames = screen.getByTestId("similar-names-list")
  const childNodes = similarTypistNames?.childNodes
  expect(childNodes?.length).toEqual(3)
})
