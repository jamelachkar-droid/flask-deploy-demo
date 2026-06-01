variable "render_api_key" {
  description = "Clé API Render"
  type        = string
  sensitive   = true
}

variable "render_owner_id" {
  description = "Owner ID du compte Render (team ou user ID)"
  type        = string
}

variable "image_url" {
  description = "URL complète de l'image Docker sur GHCR"
  type        = string
}

variable "github_username" {
  description = "Ton nom d'utilisateur GitHub (en minuscules)"
  type        = string
}