# Docker Bake 

docker bake is a high-level build command introduced by Docker as part of the Buildx plugin. It allows you to define and run complex builds for multi-platform images, multiple targets, and various configurations from a single declarative file, typically docker-bake.hcl or docker-bake.json.

## Think of it as docker-compose but for building images.

## 🔧 Why Use docker bake?

When you have:
- Multiple Dockerfiles or build targets
- Multi-platform builds (linux/amd64, linux/arm64)
- Different image variants (e.g., dev, prod)
- Reusable build configurations

## docker bake simplifies the build process by batching and orchestrating multiple builds.

## 📄 Example docker-bake.hcl:
```hcl
group "default" {
  targets = ["app", "db"]
}

target "app" {
  context = "./app"
  dockerfile = "Dockerfile"
  tags = ["myapp:latest"]
}

target "db" {
  context = "./db"
  dockerfile = "Dockerfile"
  tags = ["mydb:latest"]
}
```


## 🧩 Key Features:
| Feature              | Description                                            |
| -------------------- | ------------------------------------------------------ |
| **Multi-target**     | Build multiple images at once.                         |
| **Multi-platform**   | Easily define platform-specific builds (`--platform`). |
| **Shared variables** | Define args, envs, etc., in one place.                 |
| **Grouped builds**   | Run logical groups of builds.                          |
| **JSON or HCL**      | Use JSON (CI-friendly) or HCL (developer-friendly).    |


## >_ Commands
```bash
docker buildx bake                        # Uses default group
docker buildx bake app db                 # Build specific targets
docker buildx bake --file mybake.hcl      # Use custom file
docker buildx bake --push --set *.platform=linux/arm64
```
