const { test, expect } = require("@playwright/test");

// Skeleton smoke test: proves the Playwright toolchain is wired and the Phoenix
// application boots and serves a page in a real browser. Feature-level
// onboarding scenarios are added by their own tasks in this slice.
test("application boots and serves the home page", async ({ page }) => {
  const response = await page.goto("/");
  expect(response, "expected a response from the home page").not.toBeNull();
  expect(
    response.status(),
    "home page should respond with a non-error status",
  ).toBeLessThan(400);
});
