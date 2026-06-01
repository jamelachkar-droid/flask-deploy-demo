terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.3"
    }
  }
}

provider "render" {
  api_key  = var.render_api_key
  owner_id = var.render_owner_id
}

resource "render_web_service" "flask_app" {
  name   = "flask-deploy-demo"
  plan   = "free"
  region = "frankfurt"

  runtime_source = {
    image = {
      image_url = "ghcr.io/jamelachkar-droid/flask-deploy-demo"
      tag       = "latest"
    }
  }

  env_vars = {
    PORT = {
      value = "5000"
    }
    APP_NAME = {
      value = "flask-deploy-demo"
    }
    GITHUB_USER = {
      value = var.github_username
    }
  }

  disk = null
}