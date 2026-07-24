// Playwright configuration for SDD Orchestrator end-to-end browser tests.
//
// The web server is the real Phoenix application started through mise so the
// pinned Elixir/Erlang toolchain is used. `reuseExistingServer` lets a developer
// keep `mix phx.server` running locally while iterating on tests.
const { defineConfig, devices } = require("@playwright/test");

const baseURL = "http://localhost:4000";

module.exports = defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL,
    trace: "on-first-retry",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
  ],
  webServer: {
    command: "mise exec -- mix phx.server",
    cwd: "..",
    url: baseURL,
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
});
