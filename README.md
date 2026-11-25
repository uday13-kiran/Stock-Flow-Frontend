# StockFlow Frontend

A React + Vite inventory workspace using a warm **Cream Canvas**, **Forest Green** accents, and restrained glass surfaces. The UI is intentionally product-focused and human-designed rather than an AI-themed dashboard.

## Run locally

1. Start the FastAPI backend after applying `backend-fix/main.py` to the backend project (see below).
2. Copy `.env.example` to `.env` if you want to override the API address.
3. Install and start the frontend:

   ```bash
   npm install
   npm run dev
   ```

4. Open `http://localhost:5173`.

Default API base: `http://127.0.0.1:8000`.

## Backend endpoints verified against the uploaded Stock Flow source

| Screen / action | Method | Exact backend path | Auth |
|---|---:|---|---|
| Create organization + first user | POST | `/auth/signup` | No |
| Sign in | POST | `/auth/login` | No |
| Dashboard summary | GET | `/dashboard/` | Bearer token |
| List products | GET | `/products/` | Bearer token |
| Create product | POST | `/products/` | Bearer token |
| Read one product | GET | `/products/{product_id}` | Bearer token |
| Update product | PUT | `/products/{product_id}` | Bearer token |
| Delete product | DELETE | `/products/{product_id}` | Bearer token |

### Request / response contracts used by the UI

- Signup sends `{ email, password, organization_name }`. The backend returns a success message and IDs; the UI then asks the user to sign in.
- Login sends `{ email, password }`. The UI stores the returned `access_token` and sends it as `Authorization: Bearer <token>` for protected routes.
- Product create/update sends `name`, `sku`, `description`, `quantity`, `cost_price`, `selling_price`, and `low_stock_threshold`.
- Dashboard reads `total_products`, `total_quantity`, `low_stock_count`, and `low_stock_products`.
- Product responses include `id`, `name`, `sku`, `description`, `quantity`, `cost_price`, `selling_price`, `low_stock_threshold`, and `organization_id`.

No sales, purchase, supplier, warehouse, or analytics endpoints exist in the uploaded backend routes, so the frontend does not invent those screens or display fabricated metrics.

## Backend startup fix

The uploaded backend `main.py` calls `app.add_middleware(...)` before `app = FastAPI(...)`, which raises `NameError`. A corrected version is included at `backend-fix/main.py`. Replace the backend project's root `main.py` with that file.

The corrected file allows both `http://localhost:5173` and `http://127.0.0.1:5173`. For a deployed frontend, set the backend environment variable `FRONTEND_ORIGINS` to a comma-separated list of allowed origins, for example:

```text
FRONTEND_ORIGINS=https://your-app.vercel.app,http://localhost:5173,http://127.0.0.1:5173
```

Keep your actual `DATABASE_URL` and `SECRET_KEY` in the backend environment; do not put them in the frontend `.env`.
