import { render, screen } from "@testing-library/react"
import HomePage from "./HomePage"

it("Test name label is rendered", () => {
  render(<HomePage />)
  const message = screen.queryByText("Name")
  expect(message).toBeVisible()
})
