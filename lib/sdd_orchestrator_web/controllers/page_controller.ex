defmodule SddOrchestratorWeb.PageController do
  use SddOrchestratorWeb, :controller

  def home(conn, _params) do
    render(conn, :home)
  end
end
