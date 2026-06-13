import { useEffect, useState } from "react";

const API_BASE_URL = "/api";

function App() {
  const [systemInfo, setSystemInfo] = useState(null);
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState("");

  async function loadData() {
    try {
      setError("");

      const systemResponse = await fetch(`${API_BASE_URL}/system-info`);
      if (!systemResponse.ok) {
        throw new Error("Failed to load system information");
      }

      const ordersResponse = await fetch(`${API_BASE_URL}/orders`);
      if (!ordersResponse.ok) {
        throw new Error("Failed to load orders");
      }

      const systemData = await systemResponse.json();
      const ordersData = await ordersResponse.json();

      setSystemInfo(systemData);
      setOrders(ordersData.items);
    } catch (err) {
      setError(err.message);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  return (
    <main className="page">
      <section className="hero">
        <p className="eyebrow">Kubernetes Local Demo</p>
        <h1>KubeOps Demo</h1>
        <p className="subtitle">
          A small full-stack app prepared for Docker and Kubernetes deployment.
        </p>

        <button onClick={loadData}>Refresh Backend Data</button>
      </section>

      {error && <div className="error">Error: {error}</div>}

      {systemInfo && (
        <section className="grid">
          <InfoCard label="Service" value={systemInfo.service} />
          <InfoCard label="Version" value={systemInfo.version} />
          <InfoCard label="Environment" value={systemInfo.environment} />
          <InfoCard label="Pod / Hostname" value={systemInfo.podName} />
          <InfoCard label="Status" value={systemInfo.status} />
          <InfoCard
            label="Secret Configured"
            value={systemInfo.secretConfigured ? "Yes" : "No"}
          />
          <InfoCard
            label="Database Ready"
            value={systemInfo.databaseReady ? "Yes" : "No"}
          />
          <InfoCard label="Server Time UTC" value={systemInfo.serverTimeUtc} />
        </section>
      )}

      <section className="orders">
        <h2>Demo Orders</h2>

        <div className="orders-list">
          {orders.map((order) => (
            <article className="order-card" key={order.id}>
              <h3>{order.service}</h3>
              <p>Customer: {order.customer}</p>
              <p>Status: {order.status}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

function InfoCard({ label, value }) {
  return (
    <article className="card">
      <span>{label}</span>
      <strong>{value}</strong>
    </article>
  );
}

export default App;