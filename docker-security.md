---

## 🔐 Docker Security Best Practices

---

### 🛡️ 1. Keep Host & Docker Engine Updated

* Regularly patch the host OS and Docker engine.
* Use the latest stable Docker version.

---

### 📁 2. Set File System to Read-Only

* Minimize writable file systems inside containers.

**Example:**

```bash
docker run --read-only --tmpfs /tmp alpine sh -c 'echo "data" > /tmp/file'
```

---

### 🚫 3. Avoid `--privileged` Mode

* Never run containers with `--privileged` unless absolutely required.

---

### 🌐 4. Expose Only Necessary Ports

* Minimize open ports to reduce the attack surface.
* Avoid exposing internal service ports externally.

---

### 👤 5. Run Containers as Non-Root

* Create and use non-root users.

**Dockerfile:**

```dockerfile
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser
```

---

### 🛠️ 6. Scan Images for Vulnerabilities

* Use tools like:

  * `docker scan`
  * Trivy
  * Clair
  * Snyk

---

### 📦 7. Use Trusted Container Registries

* Pull images from verified, secure registries (e.g., Docker Hub official, AWS ECR, GitHub Container Registry).

---

### 📉 8. Limit Resource Usage

* Set CPU, memory, and PID limits per container.

**Example:**

```bash
docker run --cpus="2" --memory="512m" nginx:alpine
```

---

### 🔧 9. Drop Unnecessary Capabilities

* Start with none, and add only what's required.

**Docker:**

```bash
docker run --cap-drop ALL --cap-add CHOWN alpine
```

**Docker Compose:**

```yaml
services:
  alpine:
    image: alpine
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
```

---

### 🧱 10. Never Expose Docker Daemon Socket

* Avoid mounting `/var/run/docker.sock` into containers.

---

### 🧍‍♂️ 11. Enable User Namespaces (User Remapping)

* Prevent container-to-host privilege escalation.

**Daemon config or command:**

```bash
dockerd --userns-remap=testuser
```

---

### 🚫 12. Prevent Privilege Escalation

* Disallow new privileges in containers.

**Example:**

```bash
docker run --security-opt no-new-privileges alpine
```

---

### 🔗 13. Disable Inter-Container Communication (if not needed)

* Prevent containers from freely communicating.

**Example:**

```bash
dockerd --icc=false
```

---

### 📋 14. Set Appropriate Docker Daemon Log Level

* Keep logging level at `info` for visibility without excess verbosity.

---
