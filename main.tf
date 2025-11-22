terraform{
    required_providers{
        docker={
            source = "kreuzwerker/docker"
            version="~> 3.0"
        }
    }
}

provider "docker" {}

resource "docker_container" "student" {
    name = "student-app"
    image = "python:3.9-slim"
    command = ["sleep","60"]
    ports{
        internal = 4000
        external = 4000
    }
}