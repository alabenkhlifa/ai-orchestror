defmodule SddOrchestrator.Repo do
  use Ecto.Repo,
    otp_app: :sdd_orchestrator,
    adapter: Ecto.Adapters.Postgres
end
