### **8.1 Environment Configuration File Inclusion (Severity: High)**

This rule prohibits the inclusion of `.env` files within the version control system. Committing these files poses a significant security risk as they often contain sensitive credentials, and it breaks environment isolation by hardcoding configuration into the repository history.

**Flag when:**

* A file exists in the repository with the exact name `.env`.  
* A file exists matching the pattern `.env.*` (e.g., `.env.local`, `.env.production`, `.env.development`).  
* The file is tracked by version control (Git) rather than being excluded via `.gitignore`.

**Suggested fix:** Add all `.env` files to the project's `.gitignore` and use a secure secret management service or platform-level environment variables for configuration.

```
// Bad
# .env (file committed to the repository)
DB_PASSWORD=super_secret_password_123
STRIPE_SECRET_KEY=sk_live_51Mz...

// Good
# .gitignore
.env
.env.*
```

**Do NOT flag:**

* Template files used for documentation purposes, such as `.env.example` or `.env.template`.  
* Files within a `tests/` or `__tests__/` directory that contain non-sensitive mock environment configuration for local execution.  
* Documentation (e.g., `README.md`) that provides examples of environment variable setup.
